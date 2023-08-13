
# 1 Connect to network
import network
import random
# 2 Import BlynkLib
import BlynkLib
import time


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('B 563_2.4GHz', 'B0625976969')

BLYNK_AUTH = 'YBNMW6YNnpj6OiRHGb4Hig2QmJkl9sCB'
tmpl_id = 'TMPL6tkaL4x_u'
# initialize Blynk

blynk = BlynkLib.Blynk(BLYNK_AUTH,tmpl_id=tmpl_id)

tmr_start_time = time.time()
while True:
    blynk.run()

    t = time.time()
    if t - tmr_start_time > 1:
        print("1 sec elapsed, sending data to the server...")
        blynk.virtual_write(0,random.randint(5, 100))
        tmr_start_time += 1








