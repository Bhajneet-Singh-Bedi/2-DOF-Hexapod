import socket
import network            
import gc
import webbrowser


gc.collect()
ssid = 'RPI_PICO_AP'                  
password = '12345678'      


ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)            

while ap.active() == False:
  pass
print('Connection is successful')
print(ap.ifconfig())
def web_page():
    html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body><h1>Welcome to microcontrollerslab!</h1></body></html>"""
    return html
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    #print('Content = %s' % str(request))
    print('Content = ', request.decode('utf-8'))
    response = web_page()
    conn.send(response)
    conn.close()
    webbrowser.open("https://localhost:80")
