import RPi.GPIO as GPIO
import time

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24
SW = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)

GPIO.setup(SW[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setwarnings(False)

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)

L_Motor.start(0)
R_Motor.start(0)

try:
    while True:
        sw1Value = GPIO.input(SW[0])
        sw2Value = GPIO.input(SW[1])
        sw3Value = GPIO.input(SW[2])
        sw4Value = GPIO.input(SW[3])

        if sw1Value == 1:
            print('SW1 click')
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            L_Motor.ChangeDutyCycle(100)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            R_Motor.ChangeDutyCycle(100)
        elif sw2Value == 1:
            print('SW2 click')
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 0)
            L_Motor.ChangeDutyCycle(0)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            R_Motor.ChangeDutyCycle(100)
        elif sw3Value == 1:
            print('SW3 click')
            GPIO.output(AIN1, 1)
            GPIO.output(AIN2, 0)
            L_Motor.ChangeDutyCycle(100)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 0)
            R_Motor.ChangeDutyCycle(0)
        elif sw4Value == 1:
            print('SW4 click')
            GPIO.output(AIN1, 1)
            GPIO.output(AIN2, 0)
            L_Motor.ChangeDutyCycle(100)
            GPIO.output(BIN1, 1)
            GPIO.output(BIN2, 0)
            R_Motor.ChangeDutyCycle(100)
        else:
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

L_Motor.stop()
R_Motor.stop()
GPIO.cleanup()
