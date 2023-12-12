#!/usr/bin/python
import RPi.GPIO as GPIO
import time




def router_on():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.output(2, GPIO.HIGH)
    GPIO.cleanup()

def router_off():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.output(2, GPIO.LOW)





#main

router_on()
time.sleep(1)
router_off()
time.sleep(1)
router_on()