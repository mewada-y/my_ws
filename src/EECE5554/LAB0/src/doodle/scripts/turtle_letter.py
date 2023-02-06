#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

class turtle:
    def __init__(self):
        rospy.init_node('Lab0_turtle',anonymous=True)
        self.rate = rospy.Rate(10)
        self.PI = 3.1415926535897
        self.speed = 4
        self.vel_msg = Twist()
        self.pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
    
    def stop(self):
        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.pub.publish(self.vel_msg)
        rospy.sleep(0.5)
    
    def draw_Y(self):
        ang_speed = 20*self.speed*2*self.PI/360
        angle = 2*self.PI/360
        self.stop()
        curr_dist = 0
        curr_ang = 0
        while not rospy.is_shutdown():
            t0 = rospy.Time.now().to_sec()
            self.vel_msg.angular.z = ang_speed
            while curr_ang <= 130*angle:
                self.pub.publish(self.vel_msg)
                t1 = rospy.Time.now().to_sec()
                curr_ang = ang_speed*(t1-t0)
            self.stop()
            self.vel_msg.linear.x = self.speed
            while curr_dist <= 11:    
                self.pub.publish(self.vel_msg)
                t1 = rospy.Time.now().to_sec()
                curr_dist = self.speed*(t1-t0)
            self.stop()

            t3 = rospy.Time.now().to_sec()
            self.vel_msg.angular.z = ang_speed
            while curr_ang <= 180*angle :
                self.pub.publish(self.vel_msg)
                t1 = rospy.Time.now().to_sec()
                curr_ang = ang_speed*(t1-t3)
            self.stop()
            while curr_dist >= 11 and curr_dist <= 27:
                print("Going Straight")  
                self.vel_msg.linear.x = self.speed  
                self.pub.publish(self.vel_msg)
                t1 = rospy.Time.now().to_sec()
                curr_dist = self.speed*(t1-t0)
            self.stop()
            t4 = rospy.Time.now().to_sec()
            self.vel_msg.angular.z = ang_speed
            curr_ang = 0
            while curr_ang <= 120*angle and curr_dist >= 26:
                print("Rotating 120")
                self.pub.publish(self.vel_msg)
                t1 = rospy.Time.now().to_sec()
                curr_ang = ang_speed*(t1-t4)
            self.vel_msg.angular.z = 0
            
            while curr_dist >= 26 and curr_dist <= 38 and curr_ang >= 120*angle:
                print("Going Straight")    
                self.vel_msg.linear.x = self.speed
                self.pub.publish(self.vel_msg)
                t1 = rospy.Time.now().to_sec()
                curr_dist = self.speed*(t1-t0)
                
            self.stop()
            t5 = rospy.Time.now().to_sec()
            curr_ang = 0
            while curr_dist >=38 and curr_ang <= 180*angle:
                self.vel_msg.angular.z = ang_speed
                self.pub.publish(self.vel_msg)
                t1 = rospy.Time.now().to_sec()
                curr_ang = ang_speed*(t1-t5)
            self.vel_msg.angular.z = 0
            while curr_ang >= 180*angle and curr_dist >=38 and curr_dist <= 54:
                print("distance")
                self.vel_msg.linear.x = self.speed
                self.pub.publish(self.vel_msg)
                t1 = rospy.Time.now().to_sec()
                curr_dist = self.speed*(t1-t0)
            self.stop()
            while curr_dist >=54 and curr_dist <=70:
                self.vel_msg.linear.x = 0.9
                self.vel_msg.angular.z = 1
                self.pub.publish(self.vel_msg)
                t1 = rospy.Time.now().to_sec()
                curr_dist = self.speed*(t1-t0)
            self.stop()
            self.pub.publish(self.vel_msg)
            rospy.loginfo_once("[+] The node successfully write letter Y")
            rospy.signal_shutdown("Finished")
        rospy.spin()


if __name__ == '__main__':
    myturtle = turtle()
    try:
        myturtle.draw_Y()
    except rospy.ROSInterruptException:
        pass
