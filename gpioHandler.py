import wiringpi2 as wiringPi
import time, random
from time import sleep

wiringPi.wiringPiSetupGpio()

wiringPi.pinMode(9, 1) #clock output
wiringPi.pinMode(10, 1) #ack output
CLOCK = 9
ACK = 10

#10 data pins
PINS = [17,18,27,22,23,24,25,4,8,7]
for i in PINS:
	wiringPi.pinMode(i, 0)

time0 = time.time()
time1 = time.time()
time2 = time.time()

bits = [0,0,0,0,0,0,0,0,0,0]
words = [[],[],[],[],[],[],[],[],[],[]]

while True:
	for j in range(0,10):	
		wiringPi.digitalWrite(CLOCK, 1)
		sleep(0.00125)
		#time1 = time.time()-time0
		#print (time1-time2)*1000
		wiringPi.digitalWrite(CLOCK, 0)
		for i in range(0,10):
			bits[i] = wiringPi.digitalRead(PINS[i])
			""" simulate data input
			if j == 0 or j == 9:
				bits[i] = 1
			else:
				bits[i] = random.randint(0,1)
			"""
		words[j] = bits
		print words[j]
	wiringPi.digitalWrite(ACK, 1)
	print " "
	sleep(0.00125)
	#time2 = time.time()-time0
	#print (time2-time1)*1000
	wiringPi.digitalWrite(ACK, 0)
