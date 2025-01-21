# Runs this script first, then the client.py script on the laptop.

# server.py on Jetson Orin Nano
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = '0.0.0.0'
port = 8080

# Bind to the port
server_socket.bind((host, port))

# Start listening for connections
server_socket.listen(5)
print("Server listening on port", port)

while True:
    # Establish a connection
    client_socket, addr = server_socket.accept()
    print("Got a connection from", addr)
    
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print("Received:", data)
    
    # Print message based on received data
    if data == 'up':
        print("Moving up!")
    elif data == 'down':
        print("Moving down!")
    elif data == 'left':
        print("Moving left!")
    elif data == 'right':
        print("Moving right!")
    else:
        print("Unknown command")
    
    # Close the connection
    client_socket.close()