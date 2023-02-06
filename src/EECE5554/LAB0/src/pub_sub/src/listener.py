x#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def msg_callback(msg):
    """
    This is the message callback function whcih is called whenever any string is recived.
    Also used to alter and flip the incomming string.
    Args:
        None.
    Returns:
        None.
    """
    incomming = msg.data
    split_str = incomming.split(" ") # Logic to split and flip the string letter
    temp_val = split_str[2]
    split_str[2] = split_str[3]
    split_str[3] = temp_val
    msg.data = ' '.join(split_str)
    rospy.loginfo("I heard [+] %s",msg.data) # print the incomming string with alterations

def listener():
    """
    This is the listener function which listenes to the chatter topic   .
    Args:
        None.
    Returns:
        None.
    """
    rospy.init_node('listener',anonymous = True)
    rospy.Subscriber('chatter',String, msg_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass