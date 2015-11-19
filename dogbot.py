import motors

motors.reset()
motors.forward(2)
motors.backup(1)

motors.GPIO.cleanup()
exit()
