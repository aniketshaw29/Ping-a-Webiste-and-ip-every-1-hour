#pip install python-ping

import ping
import time

ip = "192.168.0.1" # Change this to the IP you want to ping

while True:
    response = ping.ping(ip, timeout=5)
    if response.is_reached():
        print(f"{ip} is reachable")
    else:
        print(f"{ip} is not reachable")

    time.sleep(3600) # sleep for one hour (3600 seconds)
