import threading
import serial
import time
import RPi.GPIO as GPIO

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

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

gData = ''

def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data

def go():
    global gData
    gData = ""
    print("ok go")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(100)

def back():
    global gData
    gData = ""
    print("ok back")
    GPIO.output(AIN1, 1)
    GPIO.output(AIN2, 0)
    L_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1, 1)
    GPIO.output(BIN2, 0)
    R_Motor.ChangeDutyCycle(100)

def left():
    global gData
    gData = ""
    print("ok left")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 0)
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(100)

def right():
    global gData
    gData = ""
    print("ok right")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 0)
    R_Motor.ChangeDutyCycle(0)

def stop():
    global gData
    gData = ""
    print("stop")
    L_Motor.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(0)
    
def main():
    global gData
    try:
        while True:
            if gData.find("B5") >= 0:
                go()
            elif gData.find("B4") >= 0:
                back()  
            elif gData.find("B2") >= 0:
                left()    
            elif gData.find("B0") >= 0:
                right()
            elif gData.find("B3") >= 0:
                stop()

    except KeyboardInterrupt:
        pass
    
if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()