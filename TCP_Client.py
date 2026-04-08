import socket
import ssl

# TCP client

target_host = '127.0.0.1'
target_port = 9999

# defaul SSL wrapping
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# adds SSL to the packet sent 
client = context.wrap_socket(client, server_hostname=target_host)

# Connect the client 
client.connect((target_host, target_port))

print(client.getpeername())

# send some data
client.send(b'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n')

# receive some data
response = client.recv(4096)

print(response)
