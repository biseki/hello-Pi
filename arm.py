import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gp_out = 4
GPIO.setup(gp_out, GPIO.OUT)
right = GPIO.PWM(gp_out, 50)
right.start(0)

gp_out =14
GPIO.setup(gp_out, GPIO.OUT)
left = GPIO.PWM(gp_out, 50)
left.start(0)

def default():
    right.ChangeDutyCycle(2.5)
    left.ChangeDutyCycle(12)

def oyasumi(): 
    right.ChangeDutyCycle(9.625)
    left.ChangeDutyCycle(4.875)

def tadaima():
    right.ChangeDutyCycle(2.5)
    left.ChangeDutyCycle(7.25)

def ohayou():
    right.ChangeDutyCycle(7.25)
    left.ChangeDutyCycle(7.25)

def dance():
    for i in range(5):
        right.ChangeDutyCycle(2.5)
        left.ChangeDutyCycle(4.875)
        time.sleep(0.5)

        right.ChangeDutyCycle(9.625)
        left.ChangeDutyCycle(12)
        time.sleep(0.5)
    else:
        print("Finish!")

oyasumi()
time.sleep(2)
tadaima()
time.sleep(2)
ohayou()
time.sleep(2)
dance()
default()

GPIO.cleanup()
