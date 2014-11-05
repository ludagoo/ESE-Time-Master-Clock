#!/bin/sh
# ClockLauncher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

sudo pigpiod
sudo python /home/pi/Clock/NTPClock.py
