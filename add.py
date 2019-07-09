import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)


gp_out = 4
GPIO.setup(gp_out, GPIO.OUT)
right = GPIO.PWM(gp_out, 50)
right.start(0)


gp_out = 14
GPIO.setup(gp_out, GPIO.OUT)
left = GPIO.PWM(gp_out, 50)
left.start(0)

GPIO.setup(18, GPIO.OUT)

def func1():
    while True:
        right.ChangeDutyCycle(7.25)
        time.sleep(0.5)
 
        right.ChangeDutyCycle(2.5)
        time.sleep(0.5)

def func2():
    while True:
        left.ChangeDutyCycle(2.5)
        time.sleep(0.5)
 
        left.ChangeDutyCycle(7.25)
        time.sleep(0.5)

def func3():
    while True:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)

if __name__ == "__main__":
    thread_1 = threading.Thread(target=func1)
    thread_2 = threading.Thread(target=func2)
    thread_3 = threading.Thread(target=func3)

    thread_1.start()
    thread_2.start()
    thread_3.start()

servo.stop(4, 14)
GPIO.cleanup()
