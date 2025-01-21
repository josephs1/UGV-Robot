import socket
import keyboard  # Requires `pip install keyboard`

# Define Jetson Orin Nano's IP and port
JETSON_IP = "192.168.1.189"  # Replace with the Jetson's actual IP address. Command for this is: ip addr show
PORT = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((JETSON_IP, PORT))

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((JETSON_IP, PORT))
    print("Connected to Jetson server.")

    last_key = None  # Keep track of the last key sent
    while True:
        if keyboard.is_pressed("up") and last_key != "UP":
            client_socket.sendall("UP".encode())
            last_key = "UP"
        elif keyboard.is_pressed("down") and last_key != "DOWN":
            client_socket.sendall("DOWN".encode())
            last_key = "DOWN"
        elif keyboard.is_pressed("left") and last_key != "LEFT":
            client_socket.sendall("LEFT".encode())
            last_key = "LEFT"
        elif keyboard.is_pressed("right") and last_key != "RIGHT":
            client_socket.sendall("RIGHT".encode())
            last_key = "RIGHT"
        elif not any(keyboard.is_pressed(k) for k in ["up", "down", "left", "right"]):
            last_key = None  # Reset when no arrow keys are pressed

except KeyboardInterrupt:
    print("\nDisconnected.")
    client_socket.close()
except Exception as e:
    print(f"Error: {e}")
