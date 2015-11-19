import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Left Motor Forward/Back
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

# Right Motor Forward/Back
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

# Use GPIO.setup(<pinNum>, 0) then sleep(<x>) to send power to pin for x seconds

def reset(): 
        GPIO.output(8, 0)
        GPIO.output(5, 0)
        GPIO.output(3, 0)
        GPIO.output(7, 0)

def forward(t):
        GPIO.output(7, 1)
        GPIO.output(3, 1)
        time.sleep(t)
        reset()

def backup(t):
        GPIO.output(8, 1)
        GPIO.output(5, 1)
        time.sleep(t)
        reset()

def turnRight(t):
        GPIO.output(5, 1)
        GPIO.output(7, 1)
        time.sleep(t)
        reset()

def turnLeft(t):
        GPIO.output(8, 1)
        GPIO.output(3, 1)
        time.sleep(t)
        reset()
