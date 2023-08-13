import network
from microdot import Microdot , send_file ,Response , redirect
from microdot_utemplate import render_template

from machine import Pin
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
Response.default_content_type = 'text/html'
led_status = [0,0,0,0,0,0]
led_pin = [12,11,10,26,27,28]
led = []
for i in led_pin:
    led.append(Pin(i, Pin.OUT))

@app.route('/')
def index(request):
    return render_template('index.html' , led_status = led_status)

@app.route('/<int:id>')
def index(request ,id):
    print(id)
    id = id -1
    led_status[id] = int( not led_status[id] )
    led[id].value(led_status[id])
    return redirect('/')

if __name__ == '__main__':
    do_connect()
    app.run(debug=True)