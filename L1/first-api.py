# Connect to network
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('B 563_2.4GHz', 'B0625976969')

# Make GET request
import urequests
import ujson

r = urequests.get("https://v2.jokeapi.dev/joke/Any")
r = ujson.loads(r.content)
print(r)

