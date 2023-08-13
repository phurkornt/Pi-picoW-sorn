
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

# Register virtual pin handler
@blynk.on("V1")
def v3_write_handler(value):
    print(f"pin v1 status : {value}")



while True:
    blynk.run()







