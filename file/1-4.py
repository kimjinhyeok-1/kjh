import RPi.GPIO as GPIO
import time

SW = [5, 6,13,19]
count = [0,0,0,0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)


GPIO.setup(SW[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        sw1Value = GPIO.input(SW[0])
        sw2Value = GPIO.input(SW[1])
        sw3Value = GPIO.input(SW[2])
        sw4Value = GPIO.input(SW[3])
        count
        if(sw1Value == 1):
            count[0] += 1
            print('SW1 click', count[0])
        if(sw2Value == 1):
            count[1] += 1
            print('SW2 click', count[1])
        if(sw3Value == 1):
            count[2] += 1
            print('SW3 click', count[2])
        if(sw4Value == 1):
            count[3] += 1
            print('SW4 click', count[3])

        time.sleep(0.1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()