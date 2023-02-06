#!/usr/bin/env bash

# Launch the robot
echo "Running the Publisher and Subscriber Nodes"

echo "[+] Launching Roscore"
gnome-terminal -- roscore

sleep 2
echo "[+] Launching the turtlesim node"
gnome-terminal -- rosrun turtlesim turtlesim_node

sleep 2
echo "[+] Launching the doodle node"
gnome-terminal -- rosrun doodle turtle_letter.py
