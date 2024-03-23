import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

GPIO.outpout(18, GPIO.HIGH)
time.sleep(5)
GPIO.cleanup()
