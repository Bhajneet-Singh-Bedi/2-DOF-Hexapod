from machine import Pin
import socket
import network
import gc

gc.collect()


ssid = 'RPI_PICO_AP'                  
password = '12345678'

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)  

while ap.active() == False:
  pass
print('Connection is successful')
led = Pin('LED', Pin.OUT)
led.toggle()
print(ap.ifconfig())

# HTML template for the web page
html_template = """
<!DOCTYPE html>
<html>
<body>
  <h1>Control Panel</h1>
  <button id="leftButton" onclick="sendCommand('left')">Left</button>
  <button id="rightButton" onclick="sendCommand('right')">Right</button>
  <br><br>
  <input type="range" id="slider" min="0" max="100" step="1" value="50">
  <br><br>
  <button onclick="getSliderValue()">Get Slider Value</button>
  <script>
    function sendCommand(direction) {
      // Send the direction command to the server
      fetch('/command?direction=' + direction)
        .then(response => console.log('Command sent: ' + direction))
        .catch(error => console.error('Error sending command: ' + error));
    }

    function getSliderValue() {
      // Get the value of the slider
      var sliderValue = document.getElementById('slider').value;
      console.log('Slider value: ' + sliderValue);
      
      // Send the slider value to the server
      fetch('/slider?value=' + sliderValue)
        .then(response => console.log('Slider value sent: ' + sliderValue))
        .catch(error => console.error('Error sending slider value: ' + error));
    }
  </script>
</body>
</html>
"""

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
        # Process the command (e.g., control the device)
        # TODO: Implement your logic here
    elif path.startswith('/slider?'):
        # Extract the slider value from the path
        slider_value = path.split('=')[1]
        print('Received slider value:', slider_value)
        # Process the slider value (e.g., use it for some functionality)
        # TODO: Implement your logic here

    client_socket.close()