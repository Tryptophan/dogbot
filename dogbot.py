import RPi.GPIO as GPIO
import time
import motors
import ultrasound
import sound

GPIO.setmode(GPIO.BCM)

# Main loop for polling dogbot sensors
##motors.reset()
GPIO.setup(21, GPIO.IN)
print (GPIO.input(21))

while(True):
    # Checks to see if switch to toggle freemode is on
    freeMode = (GPIO.input(21) == 1)
    while(freeMode):
        if(ultrasound.getDistance() < 80.0):
            motors.backup(.5)
            motors.turnRight(.364)
        else:
            motors.forward(.5)
        freeMode = (GPIO.input(21) == 1)
    if(ultrasound.getDistance() < 20.0):
        motors.turnLeft(.7234)
        sound.bark()

motors.GPIO.cleanup()
ultrasound.GPIO.cleanup()
exit()
