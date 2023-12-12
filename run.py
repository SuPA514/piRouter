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

#def ping_host(host):
#    ping_result = ping(target=host, count=10, timeout=2)
#
#    return {
#        'host': host,
#        'avg_latency': ping_result.rtt_avg_ms,
#        'min_latency': ping_result.rtt_min_ms,
#        'max_latency': ping_result.rtt_max_ms,
#        'packet_loss': ping_result.packet_loss
#    }

#print(ping_host('google.ca'))

#main
print("------------------------------------")

#import pyping

#response = pyping.ping('google.ca')

import subprocess
ping_response = subprocess.Popen(["/bin/ping", "-c1", "-w100", "google.ca"], stdout=subprocess.PIPE).stdout.read()

print(ping_response)

#router_on()
#time.sleep(1)
#router_off()
#time.sleep(1)
#router_on()