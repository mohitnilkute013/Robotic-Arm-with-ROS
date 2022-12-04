#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

import math
import time

class Manipulator:
    
    def __init__(self):

        self.joint1_pub = rospy.Publisher('/manipulator/joint1_position_controller/command', Float64, queue_size=1)
        self.joint2_pub = rospy.Publisher('/manipulator/joint2_position_controller/command', Float64, queue_size=1)
        self.joint3_pub = rospy.Publisher('/manipulator/joint3_position_controller/command', Float64, queue_size=1)

        self.joint1_msg = Float64()
        self.joint2_msg = Float64()
        self.joint3_msg = Float64()

        self.joint1_msg.data = 0
        self.joint2_msg.data = 0
        self.joint3_msg.data = 0

        print(self.joint1_msg.data)

        self.rate = rospy.Rate(2)

        # Arm link lengths 
        self.l1 = 0.6
        self.l2 = 0.6

        #servo rotation speed
        self.speed = 0.01

        print('Initialization Done')


    # def move_instant(self, angle):

    #     print("Moving to base angle {}".format(base_angle))

    


    def move_base_angle(self, base_angle):
        
        print("Moving to base angle {}".format(base_angle))

        while round(self.joint1_msg.data, 2) != round(base_angle, 2):
            if self.joint1_msg.data < base_angle:
                self.joint1_msg.data += self.speed
                
            elif self.joint1_msg.data > base_angle:
                self.joint1_msg.data -= self.speed

            self.joint1_pub.publish(self.joint1_msg)

            #print(self.joint1_msg.data)
            time.sleep(0.03)

        #print("Reached")

    # angle in between x and z axis
    def move_base_pose(self, distx, disty):
        base_angle = math.atan(distx/disty) # In range -pi/2 to pi/2
        
        base_angle = 1.57 - base_angle

        print("Moving to base angle {}".format(base_angle))

        while round(self.joint1_msg.data, 2) != round(base_angle, 2):
            if self.joint1_msg.data < base_angle:
                self.joint1_msg.data += self.speed
                
            elif self.joint1_msg.data > base_angle:
                self.joint1_msg.data -= self.speed

            self.joint1_pub.publish(self.joint1_msg)


            #print(self.joint1_msg.data)
            time.sleep(0.03)

        #print("Reached")
        

    def go_to_joint_angle(self, theta1, theta2):
        print("Moving to angles {} and {}".format(theta1, theta2))

    
        while round(self.joint2_msg.data, 2) != round(theta1, 2):
            if self.joint2_msg.data < theta1:
                self.joint2_msg.data += self.speed
                
            elif self.joint2_msg.data > theta1:
                self.joint2_msg.data -= self.speed

            self.joint2_pub.publish(self.joint2_msg)

            #print(self.joint2_msg.data)
            time.sleep(0.03)

        #print("Reached")

        while round(self.joint3_msg.data, 2) != round(theta2, 2):
            if self.joint3_msg.data < theta2:
                self.joint3_msg.data += self.speed
                
            elif self.joint3_msg.data > theta2:
                self.joint3_msg.data -= self.speed

            self.joint3_pub.publish(self.joint3_msg)

            #print(self.joint3_msg.data)

            time.sleep(0.03)
        #print("Reached")


    # planar inverse kinematics
    def Inv_Kin(self, x, y):
        r=(x**2)+(y**2)

        # Arm Ranges
        if r>1.9044 and r<134.56:
            
            theta2=(math.acos(((x**2)+(y**2)-(self.l1**2)-(self.l2**2))/(2*self.l1*self.l2)))
            theta1=(math.atan((y*(self.l1+self.l2*math.cos(theta2))-x*self.l2*math.sin(theta2))/(x*(self.l1+self.l2*math.cos(theta2))+y*self.l2*math.sin(theta2))))

            #print(theta1, theta2)
            # theta1 = 3.1415 - theta1
            
            return 1.57 - theta1, 3.1415 - theta2

        else:
            print("Coordinate out of range")
            return self.joint2_msg.data, self.joint3_msg.data


    def go_to_pose(self, y, z):
        print("Calculating theta1 and theta2 for y:{} z:{}".format(y,z))
        a1, a2 = self.Inv_Kin(y, z)

        #print("Moving to theta1 {} and theta2 {}".format(a1,a2))
        self.go_to_joint_angle(a1, a2)

    # def activate_gripper(self, activate):
    #     if activate:
    #         print("Gripping")
    #         self.joint4_msg.data = 60
    #     else:
    #         print("Gripper opening")
    #         self.joint4_msg.data = 120

    def get_angles(self):
        return (self.joint1_msg.data, self.joint2_msg.data, self.joint3_msg.data)

    # def __del__(self):
    #     print("Object of class Manipulator deleted.")
    #     self.deinit()

if __name__ == "__main__":
    print("heloo")

    rospy.init_node('node_joint_publisher')

    mani = Manipulator()

    while not rospy.is_shutdown():

        x = float(input("X:"))
        y = float(input("Y:"))
        z = float(input("Z:"))


        mani.move_base_angle(x)

        mani.go_to_joint_angle(y,z)

        time.sleep(2)
        
        # mani.move_base_pose(x, z)

        # calc now dist and goto position    ---doubt
        # base_hypo = math.sqrt(x**2 + z**2)

        # mani.go_to_pose(y, z)

        # mani.activate_gripper(True)

        # print("Picked")

        # mani.move_base_angle(0)
        # mani.go_to_pose(8, 8)

        # mani.activate_gripper(False)

        # print("Dropped")

    rospy.spin()
