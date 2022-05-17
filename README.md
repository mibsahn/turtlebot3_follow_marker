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

### ROS Camera Script
This script subscribes to the ROS camera node of the R200 camera, receiving the image_raw of the color and depth topics.

### Aruco Tracker Script
This script controls the detection of Aruco Markers within the images gained from the camera. It does this by importing a library of Aruco Markers that will then be compared against anything that is found to be a Marker within the image published (line 60-61).

If a marker is successfully detected, the rest of the code will detect the four corners of the marker and create a box enclosing the marker. From these corners, a centre point of the marker is calculated and displayed on the image.

### Velocity Control Script
This script take the pixel coordinate of the centre point of the marker as an input. It then calculate the average depth value around that pixel on the depth image and generate linear velocity message accordingly. It also generate angular velocity message depending on the pixel coordinate. Then it publish the message to control the Turtlebot. Proportional control is used, the further the marker are from the robot, the faster the robot move.
