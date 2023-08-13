
import urequests
import time
import ujson
import network

from machine import Pin
sw = Pin(20, Pin.IN, Pin.PULL_UP)


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('B 563_2.4GHz', 'B0625976969')


old_sw = sw.value()

while True:
    if wlan.isconnected() :
        r = urequests.get(f'http://192.168.1.100:3000/item?sw={sw.value()}')
        print(ujson.loads(r.content))
        r.close()
