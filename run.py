#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#from pythonping import ping

import platform, subprocess

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
def ping(host_or_ip, packets=1, timeout=3):
    ''' Calls system "ping" command, returns True if ping succeeds.
    Required parameter: host_or_ip (str, address of host to ping)
    Optional parameters: packets (int, number of retries), timeout (int, ms to wait for response)
    Does not show any output, either as popup window or in command line.
    Python 3.5+, Windows and Linux compatible
    '''
    # The ping command is the same for Windows and Linux, except for the "number of packets" flag.
    if platform.system().lower() == 'windows':
        command = ['ping', '-n', str(packets), '-w', str(timeout), host_or_ip]
        # run parameters: capture output, discard error messages, do not show window
        result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, creationflags=0x08000000)
        # 0x0800000 is a windows-only Popen flag to specify that a new process will not create a window.
        # On Python 3.7+, you can use a subprocess constant:
        #   result = subprocess.run(command, capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
        # On windows 7+, ping returns 0 (ok) when host is not reachable; to be sure host is responding,
        # we search the text "TTL=" on the command output. If it's there, the ping really had a response.
        return result.returncode == 0 and b'TTL=' in result.stdout
    else:
        command = ['ping', '-c', str(packets), '-w', str(timeout), host_or_ip]
        # run parameters: discard output and error messages
        result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0


ping("google.ca")
#router_on()
#time.sleep(1)
#router_off()
#time.sleep(1)
#router_on()