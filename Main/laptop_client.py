import socket
import keyboard  # Requires `pip install keyboard`
import time  # To manage the 1-second delay

# Define Jetson Orin Nano's IP and port
JETSON_IP = "192.168.1.189"  # Replace with the Jetson's actual IP address
PORT = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((JETSON_IP, PORT))

# Variable to track the last time a key press was handled
last_time = time.time()

try:
    print("Press arrow keys to send commands. Press ESC to exit.")
    while True:
        current_time = time.time()
        
        # Process keyboard input only once every second
        if current_time - last_time >= 1:
            if keyboard.is_pressed("up"):
                client_socket.sendall(b"UP")
                print("Sent: UP")
                last_time = current_time  # Update last_time after sending the message
            elif keyboard.is_pressed("down"):
                client_socket.sendall(b"DOWN")
                print("Sent: DOWN")
                last_time = current_time
            elif keyboard.is_pressed("left"):
                client_socket.sendall(b"LEFT")
                print("Sent: LEFT")
                last_time = current_time
            elif keyboard.is_pressed("right"):
                client_socket.sendall(b"RIGHT")
                print("Sent: RIGHT")
                last_time = current_time
            elif keyboard.is_pressed("esc"):
                break

        time.sleep(0.01)  # Small delay to prevent excessive CPU usage during the loop
except KeyboardInterrupt:
    pass
finally:
    client_socket.close()
    print("Connection closed.")
