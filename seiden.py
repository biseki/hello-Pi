import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

status = 0
print("start")

try:
    while True:
        value = GPIO.input(26)
        if value != status:
            print("hoge")
            print(value)
            status = value

except(KeyboardInterrupt):
    print("interrupt")

GPIO.cleanup()
