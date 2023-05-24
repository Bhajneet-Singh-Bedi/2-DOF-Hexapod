from machine import Pin
from servo import Servo
import socket
import errno
import network
import utime
import gc


check = 0
speed = 5
s1=Servo(0)
s2=Servo(1)
s3=Servo(2)
s4=Servo(3)
s5=Servo(4)
s6=Servo(5)

s7=Servo(7)
s8=Servo(8)
s9=Servo(9)
s10=Servo(10)
s11=Servo(11)
s12=Servo(12)

command = " "
direction_value=-1
speed_value=5

def main():
    global command, check
    global direction_value
    global speed_value
    gc.collect()
    # connection password and ssid.
    ssid = 'Spidey'                  
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
    #server_socket.setblocking(False)
    server_socket.bind(('', 80))
    server_socket.listen(1)

    # Main server loop
    while True:
        client_socket, addr = server_socket.accept()
        print('asdjnn')
        #print(client_socket)
        request = client_socket.recv(1024).decode()
        print('kakak')
        #print(request)
    
        #print('lala')
        # Parse the request path
        path = parse_request(request)

        if path == '/':
            # Send the HTML template as the response
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + html_template
            send_response(client_socket, response.encode())
        elif path.startswith('/command?'):
            # Extract the command from the path
            command = path.split('=')[1]
            #print('Received command:', command)
            if command == 'left' or command == 'right':
                start()
                rotate(command)
            elif command == 'start':
                start()
            elif command == 'stop':
                stop()

        elif path.startswith('/slider?'):
            # Extract the slider value from the path
            direction_value = path.split('=')[1]
            #print('Received direction value:', direction_value)
            if int(direction_value) ==  2:
                front()
            elif int(direction_value) == 1:
                stop()
        elif path.startswith('/slider2?'):
            # Extract the slider value from the path
            speed_value = path.split('=')[1]
            #print('Received speed value:', speed_value)
            speedd(int(speed_value))
        
        print(str(command)+"   "+str(direction_value)+ "  " + str(speed_value))
        client_socket.close()
        
    

def start():
    servo_Angle(90, s1)
    servo_Angle(90, s2)
    servo_Angle(90, s3)
    servo_Angle(90, s4)
    servo_Angle(90, s5)
    servo_Angle(90, s6)
    servo_Angle(90, s7)
    servo_Angle(90, s8)
    servo_Angle(90, s9)
    servo_Angle(90, s10)
    servo_Angle(90, s11)
    servo_Angle(90, s12)
    
def stop():
    servo_Angle(40, s1)
    servo_Angle(90, s2)
    servo_Angle(40, s3)
    servo_Angle(90, s4)
    servo_Angle(40, s5)
    servo_Angle(90, s6)
    servo_Angle(40, s7)
    servo_Angle(90, s8)
    servo_Angle(40, s9)
    servo_Angle(90, s10)
    servo_Angle(40, s11)
    servo_Angle(90, s12)

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
    
def rotate(cmd):
    # Rotate one leg from left hand side and other two from right hand side.
    # Then do the vice versa.
    # We have 90 degrees at nominal position.
    # Rotate 20 degrees.
    # Left leg
    # Pick Up...
    
    if str(cmd) == 'right':
        ############# Right moving...
        #1, 8,,,,,4, 10,,,,,6, 12
        
        pickLeg3(s5, s9, s1)
        for i in range(90, 59, -1):
            servo_Angle(i, s6)
            #servo_Angle(120-(90-i), s12) # -> bring from 130 to 90
            servo_Angle(i, s2)
            #servo_Angle(60+(90-i), s8) # -> bring from 50 to 90
            servo_Angle(i, s10)
            #servo_Angle(60+(90-i), s4) # -> bring from 50 to 90
            utime.sleep_ms(speed)
        putLeg3(s5, s9, s1)
        pickLeg3(s11, s3, s7)
        # Come back
        for i in range(60, 91):
            servo_Angle(i, s6)
            #servo_Angle(90+(i-60),s12) # -> bring from 90 to 130
            servo_Angle(i, s2)
            #servo_Angle(90-(i-60),s8) # -> bring from 90 to 50
            servo_Angle(i, s10)
            #servo_Angle(90-(i-60), s4) # -> bring fromm 90 to 50
            utime.sleep_ms(speed)
        putLeg3(s11, s3, s7)
        ############# Right moving...
    elif cmd == 'left':
        ############# Left moving...
        
        pickLeg3(s11, s7, s3)
        for i in range(90, 121 ):
            servo_Angle(i, s12)
            servo_Angle(i, s8)
            servo_Angle(i, s4)
            utime.sleep_ms(speed)
        putLeg3(s11, s7, s3)
        pickLeg3(s5, s9, s1)
        # Come back
        for i in range(120, 89, -1):
            servo_Angle(i, s12)
            servo_Angle(i, s8)
            servo_Angle(i, s4)
            utime.sleep_ms(speed)
        putLeg3(s5, s9, s1)
        
        ############# Left moving...
def front():
    ############# Forward moving...
    
    # Go forward
    pickLeg3(s5, s9, s1)
    for i in range(90, 59, -1):
        servo_Angle(i, s6)
        servo_Angle(120-(90-i), s12) # -> bring from 130 to 90
        servo_Angle(90+(90-i), s2)
        servo_Angle(60+(90-i), s8) # -> bring from 50 to 90
        servo_Angle(90+(90-i), s10)
        servo_Angle(60+(90-i), s4) # -> bring from 50 to 90
        utime.sleep_ms(speed)
    putLeg3(s5, s9, s1)
    pickLeg3(s11, s3, s7)
    # Come back
    for i in range(60, 91):
        servo_Angle(i, s6)
        servo_Angle(90+(i-60),s12) # -> bring from 90 to 130
        servo_Angle(120-(i-60), s2)
        servo_Angle(90-(i-60),s8) # -> bring from 90 to 50
        servo_Angle(120-(i-60), s10)
        servo_Angle(90-(i-60), s4) # -> bring fromm 90 to 50
        utime.sleep_ms(speed)
    putLeg3(s11, s3, s7)
    
    ######### Forward moving...
    
    
    
def speedd(speed_value):
    global speed
    speed = int(speed_value)

def pickLeg(servo):
    for i in range(90, 120):
        servo_Angle(i, servo)
        utime.sleep_ms(speed)
        
def putLeg(servo):
    for i in range(120, 90, -1):
        servo_Angle(i, servo)
        utime.sleep_ms(speed)
    
def pickLeg3(servo1, servo2, servo3):
    for i in range(90, 40, -1):
        servo_Angle(i, servo1)
        servo_Angle(i, servo2)
        servo_Angle(i, servo3)
        utime.sleep_ms(int(speed))
        
def putLeg3(servo1, servo2, servo3):
    for i in range(40, 90):
        servo_Angle(i, servo1)
        servo_Angle(i, servo2)
        servo_Angle(i, servo3)
        utime.sleep_ms(speed)
        

def template():
    html_template = """
    <!DOCTYPE html>
    <html>
    <body>
      <h1>Spidey Panel</h1>
      <button id="startButton" onclick="sendCommand('start')">Start</button>
      <button id="leftButton" onclick="sendCommand('left')">Left</button>
      <button id="rightButton" onclick="sendCommand('right')">Right</button>
      <button id="StopButton" onclick="sendCommand('stop')">Stop</button>
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