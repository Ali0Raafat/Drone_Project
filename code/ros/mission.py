#!/usr/bin/env python3
import rospy
from iq_gnc.py_gnc_functions import *
from sensor_msgs.msg import LaserScan
from math import cos, sin, radians, sqrt, pow

drone = gnc_api()
avoid_x = 0.0
avoid_y = 0.0
avoid = False

def laser_cb(msg):
    global avoid_x, avoid_y, avoid
    avoid_x = 0.0
    avoid_y = 0.0
    avoid = False
    d0 = 3.0
    k = 0.5
    for i in range(1, len(msg.ranges)):
        if msg.ranges[i] < d0 and msg.ranges[i] > 0.35:
            avoid = True
            x = cos(msg.angle_increment * i)
            y = sin(msg.angle_increment * i)
            u = (-0.5 * k * pow((1/msg.ranges[i]) - (1/d0), 2.0))
            avoid_x += (x*u)
            avoid_y += (y*u)

def main():
    rospy.init_node("mission", anonymous=True)
    rospy.Subscriber(name="/spur/laser/scan",
                     data_class=LaserScan,
                     queue_size=1,
                     callback=laser_cb)

    drone.wait4connect()
    drone.wait4start()
    drone.initialize_local_frame()
    drone.takeoff(3)

    # waypoints
    waypoints = [
        (0,  0,  3, 0),
        (5,  0,  3, 0),
        (5,  5,  3, 90),
        (0,  5,  3, 180),
        (0,  0,  3, 0),
    ]

    counter = 0
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.spinOnce() if False else None
        rate.sleep()
        if drone.check_waypoint_reached(3) == 1:
            if counter < len(waypoints):
                wp = waypoints[counter]
                drone.set_destination(wp[0], wp[1], wp[2], wp[3])
                counter += 1
            else:
                drone.land()
                break

        if avoid:
            cur = drone.get_current_location()
            dist = sqrt(pow(avoid_x, 2) + pow(avoid_y, 2))
            if dist > 3:
                avoid_x = (3 * (avoid_x/dist))
                avoid_y = (3 * (avoid_y/dist))
            drone.set_destination(
                avoid_x + cur.x,
                avoid_y + cur.y,
                3, 0)

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
