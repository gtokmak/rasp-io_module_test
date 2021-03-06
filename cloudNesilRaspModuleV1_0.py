import sys
import time
import signal
import threading
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

out1 = 16
out2 = 18
out3 = 36
out4 = 32
ORCODE_CE = 37

GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)
GPIO.setup(out4, GPIO.OUT)
GPIO.setup(ORCODE_CE, GPIO.OUT)

GPIO.output(out1, GPIO.LOW)
GPIO.output(out2, GPIO.LOW)
GPIO.output(out3, GPIO.LOW)
GPIO.output(out4, GPIO.LOW)
GPIO.output(ORCODE_CE, GPIO.LOW)

IN1 = 7
IN2 = 11
IN3 = 13
IN4 = 15


def getDate():
    return datetime.now().strftime('%d-%m-%Y %H:%M:%S')


def getRaspTempC():
    try:
        tFile = open('/sys/class/thermal/thermal_zone0/temp')
        temp = float(tFile.read())
        return temp / 1000
    except Exception as err:
        print('Temp Read err: ', err)
    finally:
        tFile.close()


def getInfo():
    rasptemp = getRaspTempC()
    date = getDate()
    print(f'Date:{date} Temperature:{rasptemp}')


def signal_handler(sig, freme):
    GPIO.cleanup()
    print('Application stopped')
    sys.exit()


def button_BOTH_pressed_callback(channel):
    if GPIO.input(channel):
        data = 'button_BOTH_pressed_callback channel:' + str(channel) + ' HIGH\tdate:' + getDate()
        print(data)
    else:
        data = 'button_BOTH_pressed_callback channel:' + str(channel) + ' LOW\tdate:' + getDate()
        print(data)


def raspOutput():
    while True:
        GPIO.output(out1, GPIO.HIGH)
        GPIO.output(out2, GPIO.HIGH)
        GPIO.output(out3, GPIO.HIGH)
        GPIO.output(out4, GPIO.HIGH)
        GPIO.output(ORCODE_CE, GPIO.HIGH)
        print('Output  HIGH')
        time.sleep(3)
        GPIO.output(out1, GPIO.LOW)
        GPIO.output(out2, GPIO.LOW)
        GPIO.output(out3, GPIO.LOW)
        GPIO.output(out4, GPIO.LOW)
        GPIO.output(ORCODE_CE, GPIO.LOW)
        print('Output  LOW')
        time.sleep(3)


if __name__ == '__main__':
    print(f'Raspberry pi 4 CloudNesil Input Output Modele V0.1')
    getInfo()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(IN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(IN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(IN4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(IN1, GPIO.BOTH, callback=button_BOTH_pressed_callback, bouncetime=1)
    GPIO.add_event_detect(IN2, GPIO.BOTH, callback=button_BOTH_pressed_callback, bouncetime=1)
    GPIO.add_event_detect(IN3, GPIO.BOTH, callback=button_BOTH_pressed_callback, bouncetime=1)
    GPIO.add_event_detect(IN4, GPIO.BOTH, callback=button_BOTH_pressed_callback, bouncetime=1)

    threadOutput = threading.Thread(target=raspOutput)
    threadOutput.daemon = True
    threadOutput.start()

    #     GPIO.add_event_detect(IN1, GPIO.BOTH, callback=button_BOTH_pressed_callback, bouncetime=1)
    #     GPIO.add_event_detect(IN2, GPIO.FALLING, callback=button_FALLING_pressed_callback, bouncetime=1)
    #     GPIO.add_event_detect(IN3, GPIO.RISING, callback=button_RISING_pressed_callback, bouncetime=1)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
