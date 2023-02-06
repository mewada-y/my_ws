#!/usr/bin/env bash

# Launch the robot
echo "Running the Publisher and Subscriber Nodes"

echo "[+] Launching Roscore"
gnome-terminal -- roscore

sleep 1
echo "[+] Launching the talker node"
gnome-terminal -- rosrun pub_sub talker.py

sleep 1
echo "[+] Launching the listener node"
gnome-terminal -- rosrun pub_sub listener.py
