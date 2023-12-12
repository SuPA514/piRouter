#!/usr/bin/python
import RPi.GPIO as GPIO
import time

from ping3 import ping, verbose_ping




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

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False


ping('google.ca')

#main





#router_on()
#time.sleep(1)
#router_off()
#time.sleep(1)
#router_on()