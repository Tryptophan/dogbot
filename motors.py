import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Left Motor Forward/Back
GPIO.setup(4, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)

# Right Motor Forward/Back
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

# Use GPIO.setup(<pinNum>, 0) then sleep(<x>) to send power to pin for x seconds

def reset(): 
        GPIO.output(14, 0)
        GPIO.output(3, 0)
        GPIO.output(2, 0)
        GPIO.output(4, 0)

def forward(t):
        GPIO.output(4, 1)
        GPIO.output(2, 1)
        time.sleep(t)
        reset()

def backup(t):
        GPIO.output(14, 1)
        GPIO.output(3, 1)
        time.sleep(t)
        reset()

def turnRight(t):
        GPIO.output(3, 1)
        GPIO.output(4, 1)
        time.sleep(t)
        reset()

def turnLeft(t):
        GPIO.output(14, 1)
        GPIO.output(2, 1)
        time.sleep(t)
        reset()

reset()
turnLeft(1)
