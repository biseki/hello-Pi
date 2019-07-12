import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN)

GPIO.setup(4, GPIO.OUT)
right = GPIO.PWM(4, 50)
right.start(0)

GPIO.setup(14, GPIO.OUT)
left = GPIO.PWM(14, 50)
left.start(0)

def dance():
    for i in range(5):
        right.ChangeDutyCycle(2.5)
        left.ChangeDutyCycle(4.875)
        time.sleep(0.5)

        right.ChangeDutyCycle(9.625)
        left.ChangeDutyCycle(12)
        time.sleep(0.5)

print("start")

j = 0

while j < 1.5:
    if GPIO.input(26) != 0:
        j += 0.1
    else:
        j = 0

    time.sleep(0.1)

dance()
print("finish")

GPIO.cleanup()
