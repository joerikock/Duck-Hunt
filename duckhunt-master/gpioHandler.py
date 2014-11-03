import wiringpi2 as wiringPi 
import time, random

PINS = [7,8,4,25,24,23,22,27,18,17]
CLOCK = 9
ACK = 10
CLKSPD = 1.25/1000 #difference in s between rising and falling edges of the clock

class GpioHandler(object):
        def __init__(self):
                wiringPi.wiringPiSetupGpio()

                for i in PINS:
                        wiringPi.pinMode(i, 0)
                wiringPi.pinMode(CLOCK, 1)
                wiringPi.pinMode(ACK, 1)

                self.time0 = time.time()
                self.time1 = time.time()-self.time0
                self.time2 = time.time()-self.time0

                self.bits = [0 for i in range(0,10)]
                self.words = [self.bits[:] for i in range(0,10)]

                wiringPi.digitalWrite(ACK, 1)
                time.sleep(CLKSPD)

        def updateData(self):
                print "word, content "
                for i in range(len(self.words)):                        
                        wiringPi.digitalWrite(ACK, 0)
                        wiringPi.digitalWrite(CLOCK, 1)
                        self.time1 = time.time()-self.time0
                        while self.time1-self.time2 < CLKSPD:
                                self.time1 = time.time()-self.time0
#       		print round((self.time1-self.time2)*1000,2)
                        wiringPi.digitalWrite(CLOCK, 0)
                        for j in range(len(self.bits)):
                                self.bits[j] = wiringPi.digitalRead(PINS[j])

                        self.words[i] = list(self.bits)
                        print i, self.words[i]

                        if i == 9:
                                wiringPi.digitalWrite(ACK, 1)

                        self.time2 = time.time()-self.time0                        
                        while self.time2-self.time1 < CLKSPD:
                                self.time2 = time.time()-self.time0
#       		print round((self.time2-self.time1)*1000,2)
        def getWord(i):
                return self.words[i]
""" for standalone running on Pi        
handler = GpioHandler()

while True:
	handler.updateData()
"""
