import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

print("start")

i = 0

while i < 2:
    if GPIO.input(26) != 0:
        i += 1
    time.sleep(1)

GPIO.output(18, GPIO.HIGH)
print("finish")
    
GPIO.cleanup()
