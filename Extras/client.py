# Install:
# - pygame

# client.py on your laptop
import socket
import pygame

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Check for joystick
if pygame.joystick.get_count() == 0:
    print("No joystick connected")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the IP address of the Jetson Orin Nano
host = 'jetson_ip_address'
port = 8080

# Connect to the server
client_socket.connect((host, port))

# Main loop to read controller inputs
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            if joystick.get_button(0):  # Example button
                client_socket.sendall(b'up')
            elif joystick.get_button(1):  # Example button
                client_socket.sendall(b'down')
            elif joystick.get_button(2):  # Example button
                client_socket.sendall(b'left')
            elif joystick.get_button(3):  # Example button
                client_socket.sendall(b'right')

# Close the connection
client_socket.close()
pygame.quit()