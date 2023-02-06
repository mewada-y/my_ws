#!/usr/bin/env python3

import rospy
from std_msgs.msg import String #import string from messages for string manipulation

def speaker():
    """
    This is the talker function which publishes the 'message' string.
    Args:
        None.
    Returns:
        None.
    """
    publisher = rospy.Publisher('chatter',String, queue_size=10) # Publish the data to chatter topic
    rospy.init_node('talker',anonymous=True,) # initialise a talker node
    rate = rospy.Rate(10) # specify the loop rate of ros
    while not rospy.is_shutdown():
        message = "Hello, Myself Yash Mewada" # string to be published
        rospy.loginfo("I said [+] %s" % message) # this doesnot publishes the data to chatter
        publisher.publish(message) # YES, this does.
    rospy.spin() #Spin the loop so that it doesnot enter an infinite loop and can be exited by the user.

if __name__ == '__main__':
    try:
        speaker()
    except rospy.ROSInterruptException:
        pass