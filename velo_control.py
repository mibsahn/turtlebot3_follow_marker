#!/usr/bin/env python

from PIL import Image
import rospy
from geometry_msgs.msg import Twist
import time

while True:
    with open('target.txt', 'r') as f:
            target = f.read()

    try:
        target = list(map(int,target.split(';')))
        print(target)
    except:
        rospy.init_node('robot_cleaner', anonymous=True)
        velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        vel_msg = Twist()
        velocity_publisher.publish(vel_msg)
        print('vel-published | lin_x =',vel_msg.linear.x,'| ang_z =',vel_msg.angular.z)
        continue
    
    try:
        im = Image.open('depth_img.png', 'r')
        pixel_values = list(im.getdata())
    except:
        pass
    
    x = target[1]
    y = target[0]
    val_array = []
    for h in range(x-5,x+6):
        for w in range(y-5,y+6):
            try:
                val = pixel_values[(w-1)+(h-1)*480]
                if val > 0:
                    val_array.append(val)
                # print(h,w,val)
            except:
                print('idx error')
                pass
    if val_array:
        val = sum(val_array)/len(val_array)
    print('--')

    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    vel_msg = Twist()
    
    if val > 400:
        vel_msg.linear.x = val*0.00005
    if target[0] > 260 or target[0] < 220:
        vel_msg.angular.z = -0.0005*(target[0]-240)
    
    velocity_publisher.publish(vel_msg)
    print('vel-published | lin_x =',vel_msg.linear.x,'| ang_z =',vel_msg.angular.z)
    time.sleep(0.5)