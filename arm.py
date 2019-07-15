import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
right = GPIO.PWM(4, 50)
right.start(0)

GPIO.setup(14, GPIO.OUT)
left = GPIO.PWM(14, 50)
left.start(0)

val = [2.5, 3.6875, 4.875, 6.0625, 7.25, 8.4375, 9.625, 10.8125, 12]

def default():
    right.ChangeDutyCycle(val[0])
    left.ChangeDutyCycle(val[8])

def oyasumi(): 
    right.ChangeDutyCycle(val[7])
    left.ChangeDutyCycle(val[1])

def tadaima():
    right.ChangeDutyCycle(val[5])
    left.ChangeDutyCycle(val[8])

def ohayou():
    right.ChangeDutyCycle(val[5])
    left.ChangeDutyCycle(val[3])

def dance():
    for i in range(5):
        right.ChangeDutyCycle(val[0])
        left.ChangeDutyCycle(val[3])
        time.sleep(0.5)

        right.ChangeDutyCycle(val[5])
        left.ChangeDutyCycle(val[8])
        time.sleep(0.5)

default()
time.sleep(2)
oyasumi()
time.sleep(2)
tadaima()
time.sleep(2)
ohayou()
time.sleep(2)
dance()
time.sleep(2)
default()

GPIO.cleanup()
