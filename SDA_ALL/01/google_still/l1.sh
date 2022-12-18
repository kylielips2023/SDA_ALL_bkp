#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT

cd ~/01_lol/SDA_ALL/01/google_still/

while true
do
	echo "NEW ..............."
	python3 google_let.py
done
