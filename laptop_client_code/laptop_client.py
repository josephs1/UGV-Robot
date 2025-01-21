import socket
import keyboard  # Requires `pip install keyboard`

# Define Jetson Orin Nano's IP and port
JETSON_IP = "192.168.1.189"  # Replace with the Jetson's actual IP address. Command for this is: ip addr show
PORT = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((JETSON_IP, PORT))

try:
    print("Press arrow keys to send commands. Press ESC to exit.")
    while True:
        # Listen for arrow key presses
        if keyboard.is_pressed("up"):
            client_socket.sendall(b"UP")
        elif keyboard.is_pressed("down"):
            client_socket.sendall(b"DOWN")
        elif keyboard.is_pressed("left"):
            client_socket.sendall(b"LEFT")
        # elif keyboard.is_pressed("right"):
        #     client_socket.sendall(b"RIGHT")
        elif keyboard.is_pressed("esc"):
            break
        else:
            client_socket.sendall(b"RIGHT")
except KeyboardInterrupt:
    pass
finally:
    client_socket.close()
    print("Connection closed.")
