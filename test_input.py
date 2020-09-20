import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)

try:
    while True:
        print ("DOWN(2) %d, LEFT(3) %d, UP(4) %d, RIGHT(14) %d, TOP(17) %d, BACK(27) %d" % (GPIO.input(2),GPIO.input(3),GPIO.input(4),GPIO.input(14),GPIO.input(17),GPIO.input(27)))
        time.sleep(1.0)
except:
    print ("interrupted")
finally:
    GPIO.cleanup()
