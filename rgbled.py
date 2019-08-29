import RPi.GPIO as GPIO
import time
import sys

RED = 21
GREEN = 20
BLUE = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


def set_rgb(r, g, b):
    GPIO.output(RED, r)
    GPIO.output(GREEN, g)
    GPIO.output(BLUE, b)

try:
    while True:
        set_rgb(1, 0, 0) #Red
        time.sleep(1)
        set_rgb(0, 1, 0) #Green
        time.sleep(1)
        set_rgb(0, 0, 1) #Blue
        time.sleep(1)
        set_rgb(1, 1, 0) #Yellow
        time.sleep(1)
        set_rgb(0, 1, 1) #Cyan
        time.sleep(1)
        set_rgb(1, 0, 1) #Magenta
        time.sleep(1)
        set_rgb(1, 1, 1) #White
        time.sleep(1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
