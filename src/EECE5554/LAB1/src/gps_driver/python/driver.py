#!/bin/env python3
import puck
import rospy
import argparse
from gps_driver.msg import gps_msg


"""
Author: Yash Mewada
Created: Jan 25' 2023

"""

class gps_ros():
    def __init__(self):
        rospy.init_node('gps',anonymous = True)
        param_names = rospy.get_param_names()
        arg_port = rospy.get_param("/gps/port")
        arg_port = arg_port if arg_port != 'None' else None
        self.my_gps = puck.BU_353S4(arg_port)
        self.msg = gps_msg()
        self.pub = rospy.Publisher('/gps',gps_msg,queue_size = 10)
        self.rate = rospy.Rate(10)
        rospy.loginfo_once("[o] No argument passed, considering AUTO PORT SELECTION") if not arg_port else rospy.loginfo_once("[/] Is this the port you passed -- %s",arg_port)
    
    def talker(self):
        i = 0
        while not rospy.is_shutdown():
            usf_data = self.my_gps.read_data()
            time_stamp = self.my_gps.read_time(usf_data)
            if time_stamp:
                lat,long = self.my_gps.read_lat_long(usf_data)
                utm_latlon = self.my_gps.read_utm_latlon(usf_data)
                self.msg.Header.seq = i
                self.msg.Header.stamp.secs = int(time_stamp[0:2]) * 3600 + int(time_stamp[2:4]) * 60 + int(float(time_stamp[4:6]))
                self.msg.Header.frame_id = 'GPS1_Frame'
                self.msg.Header.stamp.nsecs = int(float(time_stamp[6:])*10**9)
                self.msg.Latitude = lat
                self.msg.Longitude = long
                self.msg.Altitude = self.my_gps.read_altitude(usf_data)
                self.msg.HDOP = self.my_gps.read_hdop(usf_data)
                self.msg.UTM_easting = utm_latlon[0]
                self.msg.UTM_northing = utm_latlon[1]
                self.msg.UTC = f"{int(time_stamp[0:2])}:{int(time_stamp[2:4])}:{int(float(time_stamp[4::]))}"
                self.msg.Zone = utm_latlon[2]
                self.msg.Letter = utm_latlon[3]
                self.pub.publish(self.msg)
                i = i+1

if __name__ == '__main__':
    gps_ros = gps_ros()
    try:
        gps_ros.talker()
        rospy.spin()
    except rospy.ROSInterruptException: pass