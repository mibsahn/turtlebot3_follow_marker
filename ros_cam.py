#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg):
    print('RGB Image received!')
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "mono8")
    except CvBridgeError as e:
        print(e)
    else:
        cv2.imwrite('camera_image.jpeg', cv2_img)

def convert_depth_image(ros_image):
    cv_bridge = CvBridge()
    print('Depth Image received!')
    try:
        depth_image = cv_bridge.imgmsg_to_cv2(ros_image, 'passthrough')
    except CvBridgeError as e:
        print(e)
    depth_array = np.array(depth_image, dtype=np.float32)
    np.save("depth_img.npy", depth_array)
    depth_array = depth_array.astype(np.uint16)
    cv2.imwrite("depth_img.png", depth_array)

def main():
    rospy.init_node('image_listener')
    rospy.Subscriber("/camera/color/image_raw", Image, image_callback,queue_size=1)
    rospy.Subscriber("/camera/depth/image_raw", Image, convert_depth_image,queue_size=1)
    
    rospy.spin()

if __name__ == '__main__':
    main()