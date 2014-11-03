import wiringpi2 as wiringPi 
import time, random

wiringPi.wiringPiSetupGpio()

CLOCK = 9
ACK = 10
PINS = [17,18,27,22,23,24,25,4,8,7]

wiringPi.pinMode(CLOCK, 1)
wiringPi.pinMode(ACK, 1)
for i in PINS:
	wiringPi.pinMode(i, 0)

#time0 = time.time()
#time1 = time.time()
#time2 = time.time()

bits = [0 for i in range(0,10)]
words = [bits[:] for i in range(0,10)]

wiringPi.digitalWrite(ACK, 1)
time.sleep(0.00125)
wiringPi.digitalWrite(ACK, 0)

while True:
	for i in range(len(words)):	
		wiringPi.digitalWrite(CLOCK, 1)
		time.sleep(0.00125)
#		time1 = time.time()-time0
#		print (time1-time2)*1000
		wiringPi.digitalWrite(CLOCK, 0)
		for j in range(len(bits)):
			bits[j] = wiringPi.digitalRead(PINS[j])
			
			if i == 0 or i == 9:
				bits[j] = 1
			else:
				bits[j] = random.randint(0,1)
		
		words[i] = list(bits)
#		print i, words[i]
		if i == 9:
			wiringPi.digitalWrite(ACK, 1)
#			print "ACK = 1"
			time.sleep(0.00125)
			wiringPi.digitalWrite(ACK, 0)
#			print "ACK = 0"
		else:
			time.sleep(0.00125)
#		time2 = time.time()-time0
#		print (time2-time1)*1000
	print "word, content "
	for k in range(len(words)):
		byte = words[k]
		byte = ''.join([str(bit) for bit in byte]) 
		byte = int(byte,2) #for decimal
		print k, byte
