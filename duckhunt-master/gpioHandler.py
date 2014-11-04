"""
The GpioHandler class handles the incoming signals from the FPGA board. It reads 10 bits
on every falling edge of the clock, and stores these words in an array of 10 words.
The 10 words are received every 3 milliseconds, and contain all the information the Pi
needs to visualise the game.
"""

# This file's imports.
import wiringpi2 as wiringPi 
import time, random

# The constants this class uses.
PINS = [7,8,4,25,24,23,22,27,18,17]
CLOCK = 9
ACK = 10
# Difference in seconds between rising and falling edges of the clock
CLKSPD = 0.0/1000 

# The GpioHandler class, receiving the signals from the FPGA.
class GpioHandler(object):

        # The constructor of GpioHandler. It sets the pins and timers.
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

        # This update method is called every iteration of the main loop.
        def updateData(self):
                print "i value"
                for i in range(len(self.words)):                        
                        if wiringPi.digitalRead(ACK) != 0:
                                wiringPi.digitalWrite(ACK, 0)
                        wiringPi.digitalWrite(CLOCK, 1)

                        self.time1 = time.time()-self.time0
                        while self.time1-self.time2 < CLKSPD:
                                self.time1 = time.time()-self.time0
#                       print round((self.time1-self.time2)*1000,2)

                        wiringPi.digitalWrite(CLOCK, 0)

                        for j in range(len(self.bits)):
                                self.bits[j] = wiringPi.digitalRead(PINS[j])
			""" 
			#dummy data
                        if i == 0:
                                self.bits = [1,1,1,1,1,1,1,1,1,1]
                        elif i == 1:
                                self.bits = [0,0,1,1,0,0,1,0,0,0]
                        elif i == 2:
                                self.bits = [0,0,0,1,1,0,0,1,0,0]
                        elif i == 3:
                                self.bits = [0,1,1,1,1,1,0,1,0,0]
                        elif i == 4:
                                self.bits = [0,0,0,0,1,1,0,0,1,0]
                        elif i == 5:
                                self.bits = [0,0,0,0,0,1,0,1,0,1]
                        elif i == 6:
                                self.bits = [0,0,1,1,0,0,1,0,0,0]
                        elif i == 7:
                                self.bits = [0,0,0,1,1,0,0,1,0,0]
                        elif i == 8:
                                self.bits = [1,1,1,1,1,1,1,1,1,1] # [1,1,1,0,1,0,0,1,1,0]
                        elif i == 9:
                                self.bits = [0,1,0,0,1,1,1,0,0,1]
 			"""
			self.words[i] = list(self.bits)
                        print i, self.words[i]
                        
			if (i != 0 and self.words[i] == [1 for k in range(len(self.bits))]) or self.words[0] != [1 for k in range(0,10)] or i == max(range(len(self.words))):
				wiringPi.digitalWrite(ACK, 1)

                        self.time2 = time.time()-self.time0                        
                        while self.time2-self.time1 < CLKSPD:
                                self.time2 = time.time()-self.time0
#                       print round((self.time2-self.time1)*1000,2)

			if (i != 0 and self.words[i] == [1 for k in range(len(self.bits))]) or self.words[0] != [1 for k in range(len(self.bits))]:
				break                        

        # This method returns the words, so other classes can use them.
        def getWord(self,i):
                return self.words[i]
        
"""#for standalone running on Pi
handler = GpioHandler()
while True:
        handler.updateData()
"""
