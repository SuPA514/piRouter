#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#from pythonping import ping

from multiping import MultiPing

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



#main
print("------------------------------------")


import subprocess



def supaping(host):
    ping_result = 0
    cmdtxt = subprocess.Popen(["/bin/ping", "-c5", "-w100", host], stdout=subprocess.PIPE).stdout.read()
    print(cmdtxt)
    if "ttl" in cmdtxt:
        cmdlines = cmdtxt.split("\n")
        cmdline = cmdlines[9]
        avgtime = cmdline.split("=")[1].split("/")[1]
        ping_result = avgtime
    else:
        ping_result = 0
    return ping_result

t = supaping("dawdawgoogle.ca")
print("ping result: " + str(t))

#router_on()
#time.sleep(1)
#router_off()
#time.sleep(1)
#router_on()