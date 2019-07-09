import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gp_out = 4
GPIO.setup(gp_out, GPIO.OUT)
servo = GPIO.PWM(gp_out,50)

servo.start(0)

val = [2.5, 3.6875, 4.875, 6.0625, 7.25, 8.4375, 9.625, 10.8125, 12]

while True:
    servo.ChangeDutyCycle(val[4])
    time.sleep(0.5)

    servo.ChangeDutyCycle(val[0])
    time.sleep(0.5)

servo.stop()
GPIO.cleanup()
