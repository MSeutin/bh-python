import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object
# AF_INET: IPv4 (Address Family Internet - Default)
# SOCK_STREAM: TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

##### Send some data #####
### Request Line: GET / HTTP/1.1
## GET: HTTP Method, /: Path, HTTP/1.1: HTTP Version
### Host Header: Host: google.com
### \r\n\r\n: Double New Line - End of Request
## \r: Carriage Return, \n: New Line
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)
print(response.decode())
client.close()