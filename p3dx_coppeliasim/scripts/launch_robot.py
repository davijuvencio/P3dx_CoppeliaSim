#!/usr/bin/env python3

import os
import sys
import rospy
import time

rospy.init_node("launch_robot")

time.sleep(5)

os.system("roslaunch p3dx_description robot.launch")
