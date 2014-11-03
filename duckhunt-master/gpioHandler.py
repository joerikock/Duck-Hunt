import wiringpi2 as wiringPi 
import time, random

wiringPi.wiringPiSetupGpio()

PINS = [7,8,4,25,24,23,22,27,18,17]
CLOCK = 9
ACK = 10
CLKSPD = 250.25/1000 #difference in s between rising and falling edges of the clock

for i in PINS:
	wiringPi.pinMode(i, 0)
wiringPi.pinMode(CLOCK, 1)
wiringPi.pinMode(ACK, 1)

time0 = time.time()
time1 = time.time()-time0
time2 = time.time()-time0

bits = [0 for i in range(0,10)]
words = [bits[:] for i in range(0,10)]

wiringPi.digitalWrite(ACK, 1)
time.sleep(CLKSPD)
wiringPi.digitalWrite(ACK, 0)

while True:
	for i in range(len(words)):	
		wiringPi.digitalWrite(CLOCK, 1)
		time1 = time.time()-time0
		while time1-time2 < CLKSPD:
			time1 = time.time()-time0
#		print round((time1-time2)*1000,2)
		wiringPi.digitalWrite(CLOCK, 0)
		for j in range(len(bits)):
			bits[j] = wiringPi.digitalRead(PINS[j])
			""" 
			if i == 0 or i == 9:
				bits[j] = 1
			else:
				bits[j] = random.randint(0,1)
			"""
		word = bits
		words[i] = word
		print i, words[i]
		if i == 9:
			wiringPi.digitalWrite(ACK, 1)
			time2 = time.time()-time0
			while time2-time1 < CLKSPD:
				time2 = time.time()-time0
			wiringPi.digitalWrite(ACK, 0)
		else:
			time2 = time.time()-time0
			while time2-time1 < CLKSPD:
				time2 = time.time()-time0
#		print round((time2-time1)*1000,2)
 
	print "word, content "
#	for k in range(len(words)):
#		print k, words[k]

class Words(object)
        def getWord(i):
                return words[i]
        
