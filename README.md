ESE-Time-Master-Clock
=====================
This is a little python program to get the current time on a Raspberry Pi and bitbag a GPIO to send the current time in ESE time code. 

NTPClock.py is the actual program. 

ClockLaucher.sh is should be added to cron boot if one wants NTPClock to run at boot. It starts the pigpiod that is needed for NTPClock  then starts NTPClock.

Dependencies:
pigpio - http://abyz.co.uk/rpi/pigpio/



