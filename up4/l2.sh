#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT

#cd /root/SDA_ALL/48_firefox/

while true
do
	echo "NEW ..............."
	timeout 5m python3 van_u4u.py
done
