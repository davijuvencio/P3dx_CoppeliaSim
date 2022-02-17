#!/usr/bin/env python3

import os
import sys
import rospy

SIMULATION_SCENE_PATH = sys.argv[1]
COPPELIA_SIM_PATH = sys.argv[2] + "/" +"coppeliaSim.sh"
COPPELIA_FLAGS = "-gGUIITEMS_4 -s"
COMMAND = COPPELIA_SIM_PATH + " " + SIMULATION_SCENE_PATH + " " + COPPELIA_FLAGS

rospy.init_node("sim_node")

os.system(COMMAND)

