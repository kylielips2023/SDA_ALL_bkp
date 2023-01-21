#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT

#cd /root/SDA_ALL/48_firefox/

while true
do
	echo "NEW ..............."
	timeout 50m python3 1skill_VISA_v2.py
done
