import socket
import ssl
import threading

# TCP Server

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

# involves the server with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

print(f"[*] Listening on {bind_ip}:{bind_port}")

# this is our client-handling thread
def handle_client(client_socket):
    
    # print out what the client sends
    request = client_socket.recv(1024)

    print(f"[*] Received: {request}")

    # send back a packet
    client_socket.send(b'ACK!')
    client_socket.close()

while True:

    client, addr = server.accept()
    ssl_client = context.wrap_socket(client, server_side=True)
    print(f"[*] Accepted conection from {addr[0]}:{addr[1]}")

    # spin up our client thread  to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(ssl_client,))
    client_handler.start() 

