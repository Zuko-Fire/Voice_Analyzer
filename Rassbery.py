import RPi.GPIO as GPIO

def onPin():
    GPIO.setmode(GPIO.BCM)

    #GPIO.setup(14, GPIO.OUT)

    GPIO.setup(15, GPIO.OUT)

    #GPIO.setup(18, GPIO.OUT)

    #GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    #GPIO.output(18, GPIO.HIGH)


def offPin():
    GPIO.cleanup()
