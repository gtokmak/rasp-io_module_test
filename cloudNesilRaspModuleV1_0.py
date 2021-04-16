import time
import datetime
import argparse
import RPi.GPIO as GPIO
import sys

IN1 = None
IN2 = None
IN3 = None
IN4 = None

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

out1 = 16
out2 = 18
out3 = 36
out4 = 32
ORCODE_CE = 26

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


in1 = 7
in2 = 11
in3 = 13
in4 = 15

GPIO.setup(in1, GPIO.IN)
GPIO.setup(in2, GPIO.IN)
GPIO.setup(in3, GPIO.IN)
GPIO.setup(in4, GPIO.IN)



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


while True:
    IN1 = GPIO.input(in1)
    IN2 = GPIO.input(in2)
    IN3 = GPIO.input(in3)
    IN4 = GPIO.input(in4)
    print('IN1:'+ str(IN1) + ' IN2:'+ str(IN2) + ' IN3:'+ str(IN3) + ' IN4:'+ str(IN4))
    time.sleep(.5)
    
    