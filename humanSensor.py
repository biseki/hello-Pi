import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
def humanSensor():
    try:
        while True:    
            if GPIO.input(26) == 1:
                print("YES")
                time.sleep(1)
            else:
                print("NO")
                time.sleep(1)
    except(KeyboardInterrupt):
        print("interrupt")
    GPIO.cleanup()
humanSensor()
