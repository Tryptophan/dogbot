import motors
import switch
import ultrasound
import sound

bool freeMode = false

# Main loop for polling dogbot sensors
while (True):

    # Checks to see if the button to toggle freeMode is on
    if (switch.GPIO.input() == 1):
        freeMode = !freeMode
    
    # Runs dogbot based on freeMode setting
    if (freeMode):
        if (ultrasound.object()):
            motors.backup(2)
            motors.turnRight(1)
        else:
            motors.forward(2)
    else:
        if (ultrasound.object()):
            motors.turnLeft(3)
            sound.bark()
        
motors.GPIO.cleanup()
exit()
