import datetime, time, threading
import pigpio
import sys

pi = pigpio.pi()
clockPin = 17
pi.set_mode(clockPin, pigpio.OUTPUT)
serialData=[]

#Ints to ESE Binary
def convertToTwoBinary(number):

	if number == 0:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	elif number == 1:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))

def convertToThreeBinary(number):
	if number == 0:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))

	elif number == 1:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
	elif number == 2:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	elif number == 3:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
	elif number == 4:
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	elif number == 5:
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))

def convertToFourBinary(number):
	if number == 0:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	elif number == 1:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
	elif number == 2:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	elif number == 3:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
	elif number == 4:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	elif number == 5:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
	elif number == 6:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	elif number == 7:
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
	elif number == 8:
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	elif number == 9:
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
		
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))

def update():
	currentTime = datetime.datetime.now()
	threading.Timer(1-(1/currentTime.microsecond), update).start()
	serialData[:]=[]
	hour = currentTime.hour
	minute = currentTime.minute
	second = currentTime.second

	#HOURS
	if hour >= 12:
		#PM
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	
		serialData.append(pigpio.pulse(1<<20, 0, 240))
		serialData.append(pigpio.pulse(0, 1<<20, 65))
	
		if hour > 12:
			#Convert 24hr to 12hr
			hour = hour - 12
	else:
		#AM
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))
	
		serialData.append(pigpio.pulse(1<<20, 0, 65))
		serialData.append(pigpio.pulse(0, 1<<20, 240))


	if hour >= 10:
		#First Digit
		convertToTwoBinary(1)
		#Second Digit
		convertToFourBinary(int(str(hour)[1]))
	else:

		#First Digit
		convertToTwoBinary(0)
		#Second Digit
		convertToFourBinary(hour)

	#MINUTES
	if minute < 10:
		#Third Digit
		convertToThreeBinary(0)
		#Fourth Digit
		convertToFourBinary(minute)

	else:
		#Third Digit
		convertToThreeBinary(int(str(minute)[0]))
		#Fourth Digit
		convertToFourBinary(int(str(minute)[1]))

	#SECONDS
	if second < 10:
		#Fith Digit
		convertToThreeBinary(0)
		#Sixth Digit
		convertToFourBinary(second)

	else:
		#Fith Digit
		convertToThreeBinary(int(str(second)[0]))
		#Sixth Digit
		convertToFourBinary(int(str(second)[1]))
	
	pi.wave_clear() # clear any existing waveforms

	pi.wave_add_generic(serialData)
	eseTime = pi.wave_create()

	pi.wave_send_once(eseTime)

update()
