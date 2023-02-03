#pip install requests
import requests
import time

url = "https://www.google.com" # Change this to the URL you want to ping

while True:
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} is reachable")
        else:
            print(f"{url} returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{url} is not reachable ({e})")

    time.sleep(3600) # sleep for one hour (3600 seconds)
