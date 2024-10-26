import RPi.GPIO as GPIO
import time

SW1 = 5
click = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)



GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        sw1Value = GPIO.input(SW1)

        if(sw1Value == 1):
            click = True
        print (1 if click else 0)

        time.sleep(0.1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()