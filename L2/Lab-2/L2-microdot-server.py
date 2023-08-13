import network
from microdot import Microdot

# Replace the following with your WIFI Credentials
SSID = "B 563_2.4GHz"
SSI_PASSWORD = "B0625976969"
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to your wifi...")

app = Microdot()
@app.route('/')
def index(request):
    return 'Hello, world!'

if __name__ == '__main__':
    do_connect()
    app.run(debug=True)
