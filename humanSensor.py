import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(26, GPIO.IN)

def light_on():
    GPIO.output(18, GPIO.HIGH)

def light_off():
    GPIO.output(18, GPIO.LOW)


while True:    
    if GPIO.input(26) == 1:
        print("YES")
        light_on()
        time.sleep(3)
        light_off()
    else:
        print("NO")
        time.sleep(1)
GPIO.cleanup()

