import time
import RPi.GPIO as GPIO



def getDistance():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Code from raspberrypi-spy.co.uk, Author: Matt

    GPIO_TRIGGER = 23
    GPIO_ECHO = 24

    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
        
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5)
    
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    
    while (GPIO.input(GPIO_ECHO) == 0):
        start = time.time()

    while(GPIO.input(GPIO_ECHO) == 1):
        stop = time.time()
        
    elapsed = stop - start
    distance = elapsed * 34000
    distance /= 2
    return distance

print (getDistance())
