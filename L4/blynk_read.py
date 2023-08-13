
# 1 Connect to network
import network
import random

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('B 563_2.4GHz', 'B0625976969')

# 2 Make GET request
import urequests
import ujson

token = 'YBNMW6YNnpj6OiRHGb4Hig2QmJkl9sCB'
pin = 'v0'

while True:
    value = random.randint(0, 100)
    r = urequests.get(f"https://blynk.cloud/external/api/update?token={token}&pin={pin}&value={value}")
    r.close()
    print("DONE : " , value)





