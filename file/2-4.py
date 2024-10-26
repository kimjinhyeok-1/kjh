import RPi.GPIO as GPIO
import time

BUZZER = 12
SW = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setwarnings(False)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, 261)  

try:
    while True:
        sw1Value = GPIO.input(SW[0])
        sw2Value = GPIO.input(SW[1])
        sw3Value = GPIO.input(SW[2])
        sw4Value = GPIO.input(SW[3])

        if sw1Value == 1:
            p.start(50) 
            p.ChangeFrequency(262)
            time.sleep(0.2)
            p.stop()  
        elif sw2Value == 1:
            p.start(50)
            p.ChangeFrequency(294)
            time.sleep(0.2)
            p.stop()
        elif sw3Value == 1:
            p.start(50)
            p.ChangeFrequency(330)
            time.sleep(0.2)
            p.stop()
        elif sw4Value == 1:
            p.start(50)
            p.ChangeFrequency(349)
            time.sleep(0.2)
            p.stop()

        time.sleep(0.2)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
