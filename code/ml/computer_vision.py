"""
Fire Detection Web App
======================
YOLOv8-based fire detection with distance estimation.
Supports image upload and live camera input.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Optional

import cv2
import numpy as np
import streamlit as st
from ultralytics import YOLO
from dotenv import load_dotenv

load_dotenv()

# ──────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────
logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────
@dataclass
class AppConfig:
    model_path: str = os.getenv("MODEL_PATH", "models/best.pt")
    focal_length: float = float(os.getenv("FOCAL_LENGTH", "1000.0"))
    real_fire_size: float = float(os.getenv("REAL_FIRE_SIZE", "10.0"))
    default_conf: float = float(os.getenv("DEFAULT_CONF", "0.40"))
    box_color: tuple[int, int, int] = (0, 200, 100)
    text_color: tuple[int, int, int] = (255, 255, 255)
    font_scale: float = 0.6
    line_thickness: int = 2


CONFIG = AppConfig()


# ──────────────────────────────────────────────
# Distance Estimator
# ──────────────────────────────────────────────
class DistanceEstimator:
    """
    Estimates distance to a detected object using the thin-lens formula:
        D = (F × H_real) / H_pixels
    where F is focal length (px), H_real is real size (cm),
    and H_pixels is bounding-box height in pixels.

    NOTE: This is an approximation. For precise results, calibrate F using
    a known object at a known distance.
    """

    def __init__(self, focal_length: float, real_size: float) -> None:
        self.focal_length = focal_length
        self.real_size = real_size

    def compute(self, bbox_height: int) -> Optional[float]:
        """Return estimated distance in metres, or None if invalid."""
        if bbox_height <= 0:
            return None
        distance_cm = (self.focal_length * self.real_size) / bbox_height
        return round(distance_cm / 100, 2)   # convert cm → m


# ──────────────────────────────────────────────
# Model Loader
# ──────────────────────────────────────────────
@st.cache_resource(show_spinner="Loading YOLOv8 model…")
def load_model(path: str) -> YOLO:
    """Load and cache the YOLOv8 model."""
    try:
        if not os.path.exists(path):
            logger.warning("Custom model not found at %s. Using default YOLOv8n.", path)
            model = YOLO("yolov8n.pt")
        else:
            model = YOLO(path)
        logger.info("Model loaded from: %s", path)
        return model
    except Exception as exc:
        logger.error("Failed to load model: %s", exc)
        st.error(
            f" Could not load model.\n\n{exc}"
        )
        st.stop()


# ──────────────────────────────────────────────
# Detection Logic
# ──────────────────────────────────────────────
def run_detection(
    frame: np.ndarray,
    model: YOLO,
    estimator: DistanceEstimator,
    conf_threshold: float,
) -> tuple[np.ndarray, list[dict]]:
    """
    Run YOLOv8 inference on a frame and annotate detections.

    Returns:
        annotated_frame: BGR image with bounding boxes drawn.
        detections: list of dicts with keys {conf, distance, bbox}.
    """
    results = model(frame, conf=conf_threshold, verbose=False)
    detections: list[dict] = []

    for result in results:
        if result.boxes is None:
            continue

        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            bbox_height = y2 - y1
            distance = estimator.compute(bbox_height)

            # Build label
            label = f" Fire  {conf:.0%}"
            if distance is not None:
                label += f"  |  ~{distance} m"

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x1, y1), (x2, y2),
                CONFIG.box_color,
                CONFIG.line_thickness,
            )

            # Draw label background
            (text_w, text_h), baseline = cv2.getTextSize(
                label,
                cv2.FONT_HERSHEY_SIMPLEX,
                CONFIG.font_scale,
                CONFIG.line_thickness,
            )
            label_y = max(y1 - 6, text_h + baseline)
            cv2.rectangle(
                frame,
                (x1, label_y - text_h - baseline),
                (x1 + text_w, label_y),
                CONFIG.box_color,
                cv2.FILLED,
            )

            # Draw label text
            cv2.putText(
                frame, label,
                (x1, label_y - baseline // 2),
                cv2.FONT_HERSHEY_SIMPLEX,
                CONFIG.font_scale,
                CONFIG.text_color,
                CONFIG.line_thickness,
                cv2.LINE_AA,
            )

            detections.append({"conf": conf, "distance": distance, "bbox": (x1, y1, x2, y2)})

    return frame, detections


# ──────────────────────────────────────────────
# Stats Panel
# ──────────────────────────────────────────────
def show_stats(detections: list[dict]) -> None:
    """Render detection statistics below the image."""
    n = len(detections)
    if n == 0:
        st.success(" No fire detected.")
        return

    st.error(f" Fire detected — **{n}** instance(s)")

    cols = st.columns(3)
    avg_conf = sum(d["conf"] for d in detections) / n
    cols[0].metric("Detections", n)
    cols[1].metric("Avg Confidence", f"{avg_conf:.0%}")

    distances = [d["distance"] for d in detections if d["distance"] is not None]
    if distances:
        cols[2].metric("Closest (~m)", f"{min(distances)} m")

    with st.expander(" Detection details"):
        for i, det in enumerate(detections, 1):
            dist_str = f"{det['distance']} m" if det["distance"] is not None else "N/A"
            st.write(f"**#{i}** — Confidence: `{det['conf']:.2%}` | Distance: `{dist_str}`")


# ──────────────────────────────────────────────
# Page Layout
# ──────────────────────────────────────────────
def build_sidebar() -> tuple[str, float]:
    """Render sidebar controls; returns (input_mode, conf_threshold)."""
    st.sidebar.title(" Settings")

    input_mode = st.sidebar.radio(
        "Input source",
        [" Upload Image", " Camera Snapshot"],
        index=0,
    )

    conf_threshold = st.sidebar.slider(
        "Confidence threshold",
        min_value=0.10,
        max_value=0.95,
        value=CONFIG.default_conf,
        step=0.05,
        help="Detections below this score are ignored.",
    )

    st.sidebar.markdown("---")
    st.sidebar.caption(
        "Model: YOLOv8 custom (`best.pt`)\n\n"
        "Distance estimation is approximate — "
        "calibrate focal length for accurate results."
    )

    return input_mode, conf_threshold


def main() -> None:
    # ── Page config ──────────────────────────────
    st.set_page_config(
        page_title="Fire Detection",
        page_icon="🔥",
        layout="wide",
    )

    # ── Header ───────────────────────────────────
    st.title(" Fire Detection System")
    st.caption("Powered by YOLOv8 · Real-time fire localisation & distance estimation")
    st.markdown("---")

    # ── Load model & estimator ───────────────────
    model = load_model(CONFIG.model_path)
    estimator = DistanceEstimator(CONFIG.focal_length, CONFIG.real_fire_size)

    # ── Sidebar ──────────────────────────────────
    input_mode, conf_threshold = build_sidebar()

    # ── Main content ─────────────────────────────
    col_img, col_info = st.columns([3, 1])

    # ── Upload Image ─────────────────────────────
    if "Upload" in input_mode:
        uploaded = st.file_uploader(
            "Upload an image (JPG / PNG)",
            type=["jpg", "jpeg", "png"],
            help="The image will be analysed for fire using YOLOv8.",
        )

        if uploaded is not None:
            file_bytes = np.frombuffer(uploaded.read(), dtype=np.uint8)
            frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            if frame is None:
                st.error(" Could not decode the uploaded image. Try another file.")
                return

            with st.spinner("Running detection…"):
                annotated, detections = run_detection(frame, model, estimator, conf_threshold)

            with col_img:
                st.image(annotated, channels="BGR", use_container_width=True)

            with col_info:
                show_stats(detections)

    # ── Camera Snapshot ───────────────────────────
    else:
        st.info(
            "📸 Click **Take Photo** to capture a frame from your webcam. "
            "Detection runs automatically after capture."
        )
        img_file = st.camera_input("Take a photo")

        if img_file is not None:
            file_bytes = np.frombuffer(img_file.read(), dtype=np.uint8)
            frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            if frame is None:
                st.error(" Could not decode the camera frame.")
                return

            with st.spinner("Running detection…"):
                annotated, detections = run_detection(frame, model, estimator, conf_threshold)

            with col_img:
                st.image(annotated, channels="BGR", use_container_width=True)

            with col_info:
                show_stats(detections)


# ──────────────────────────────────────────────
# Entry Point
# ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
