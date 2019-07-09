import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

while True:
	print GPIO.input(26)
	time.sleep(1)

GPIO.cleanup()
