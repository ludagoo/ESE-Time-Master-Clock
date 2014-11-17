#!/bin/sh
# ClockLauncher.sh
# navigate to home directory, then to /home/pi/ESE-Time-Master-Clock directory, then execute python script

sudo pigpiod
sudo python /home/pi/ESE-Time-Master-Clock/NTPClock.py
