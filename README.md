# Turtlebot3 following marker

## Required installation

1. Linux environment with ROS installed
2. python3 and the following packages rospy, opencv-python, numpy

## Launch the turtlebot
Initialize the robot by launching turtlebot3_bringup and realsense camera

1. Start roscore on your PC

2. ssh into turtlebot and launch the following files
	`roslaunch turtlebot3_bringup turtlebot3_robot.launch`
	`roslaunch realsense_camera r200_nodelet_default.launch`

3. Go back to your PC and launch these python scripts seperately and simutanously
	`python3 ros_cam.py`
	`python3 aruco_tracker.py`
	`python3 velo_control.py`
