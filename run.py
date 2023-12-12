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

def ping(host,n = 0):
    if(n>0):
        avg = 0
        for i in range (n):
            avg += ping(host)
        avg = avg/n
    # Create a MultiPing object to test hosts / addresses
    mp = MultiPing([host])

    # Send the pings to those addresses
    mp.send()

    # With a 1 second timout, wait for responses (may return sooner if all
    # results are received).
    responses, no_responses = mp.receive(1)


    for addr, rtt in responses.items():
        RTT = rtt


    if no_responses:
        # Sending pings once more, but just to those addresses that have not
        # responded, yet.
        mp.send()
        responses, no_responses = mp.receive(1)
        RTT = -1

    return RTT


ping("google.ca")
#router_on()
#time.sleep(1)
#router_off()
#time.sleep(1)
#router_on()