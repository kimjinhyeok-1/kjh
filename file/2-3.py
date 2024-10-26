import RPi.GPIO as GPIO
import time

BUZZER = 12
SW1 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)

p = GPIO.PWM(BUZZER,261)
p.start(50)

try:
    while True:
        p.start(50)
        sw1Value = GPIO.input(SW1)

        if(sw1Value == 1):
            p.ChangeFrequency(262)
            time.sleep(0.2)
        p.stop()
        time.sleep(0.2)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()