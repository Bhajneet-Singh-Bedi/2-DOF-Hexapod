from machine import Pin
#from servo import Servo
import socket
import network
import utime
import gc

speed = 5

def main():
    print('lala')
    gc.collect()
    # connection password and ssid.
    ssid = 'RPI_PICO_AP'                  
    password = '12345678'
    
    # Creating Soft Access Point
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)  
    
    while ap.active() == False:
      pass
    
    # To safe check.
    print('Connection is successful')
    led = Pin('LED', Pin.OUT)
    led.on()
    print(ap.ifconfig())
    
    
    # Template
    html_template = template()

    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 80))
    server_socket.listen(1)
    
    # Function to parse HTTP requests
    def parse_request(request):
        try:
            request_line = request.split('\r\n')[0]
            path = request_line.split(' ')[1]
            return path
        except:
            return None

    # Function to send HTTP response
    def send_response(client_socket, response):
        client_socket.send(response)

    # Main server loop
    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024).decode()

        # Parse the request path
        path = parse_request(request)

        if path == '/':
            # Send the HTML template as the response
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + html_template
            send_response(client_socket, response.encode())
        elif path.startswith('/command?'):
            # Extract the command from the path
            command = path.split('=')[1]
            print('Received command:', command)
            rotate(command)

        elif path.startswith('/slider?'):
            # Extract the slider value from the path
            direction_value = path.split('=')[1]
            print('Received direction value:', direction_value)
            front_back()

        elif path.startswith('/slider2?'):
            # Extract the slider value from the path
            speed_value = path.split('=')[1]
            print('Received speed value:', speed_value)
            speedd(speed_value)
    

        client_socket.close()
    
    
    
def rotate(cmd):
    pass
    # Rotate one leg from left hand side and other two from right hand side.
    # Then do the vice versa.
    # We have 90 degrees at nominal position.
    # Rotate 20 degrees.
    # Left leg
    # Pick Up...
    for i in range(90, 120):
        servo_Angle(i, s)
        utime.sleep_ms(1)
        servo_Angle(i, s)
        utime.sleep_ms(1)
        servo_Angle(i, s)
        utime.sleep_ms(speed)
    # Move 20 degrees
    for i in range(90, 110):
        servo_Angle(i, s)
        utime.sleep_ms(1)
        servo_Angle(90-i, s)
        utime.sleep_ms(speed)
    # Go down
    for i in range(120, 90):
        servo_Angle(i, s)
        utime.sleep_ms(speed)
    # Come back 20 degrees
    for i in range(110, 90):
        servo_Angle(i, s)
        utime.sleep_ms(speed)

def front_back():
    pass

def speedd(speed_value):
    speed = speed_value

def template():
    html_template = """
    <!DOCTYPE html>
    <html>
    <body>
      <h1>Spidey Panel</h1>
      <button id="leftButton" onclick="sendCommand('left')">Left</button>
      <button id="rightButton" onclick="sendCommand('right')">Right</button>
      <br><br>
      <input type="range" id="slider" min="0" max="2" step="1" value="1">
      <br><br>
      <button onclick="getDirection()">Direction</button>
      <br><br>
      <input type="range" id="slider2" min="2" max="10" step="2" value="5">
      <br><br>
      <button onclick="getSpeed()">Speed</button>
      <script>
        function sendCommand(direction) {
          // Send the direction command to the server
          fetch('/command?direction=' + direction)
            .then(response => console.log('Command sent: ' + direction))
            .catch(error => console.error('Error sending command: ' + error));
        }

        function getDirection() {
          // Get the value of the direction
          var directionValue = document.getElementById('slider').value;
          console.log('Direction value: ' + directionValue);
          
          // Send the slider value to the server
          fetch('/slider?value=' + directionValue)
            .then(response => console.log('direction value sent: ' + directionValue))
            .catch(error => console.error('Error sending direction value: ' + error));
        }
        function getSpeed() {
          // Get the value of the speed
          var speedValue = document.getElementById('slider2').value;
          console.log('Speed value: ' + speedValue);
          
          // Send the slider value to the speed
          fetch('/slider2?value=' + speedValue)
            .then(response => console.log('Speed value sent: ' + speedValue))
            .catch(error => console.error('Error sending speed value: ' + error));
        }
      </script>
    </body>
    </html>
    """
    return html_template

def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle, s):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value


main()