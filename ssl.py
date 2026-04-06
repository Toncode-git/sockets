import socket
import ssl

context = ssl.create_default_context()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = context.wrap_socket(client, server_hostname='www.github.com')
client.connect(('www.github.com', 443))
client.send(b'GET / HTTP/1.1\r\nHost: www.github.com\r\n\r\n')

response = client.recv(4096)
print(response)