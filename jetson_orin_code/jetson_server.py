# Used sudo apt install python3-serial on jetson
import socket
import serial

# Set up serial connection to Arduino
SERIAL_PORT = "/dev/ttyACM0"  # Replace with the Arduino's serial port
# Command for scanning ports: ls /dev/ttyACM*
# Giving write permissions: sudo chmod 666 /dev/ttyACM0
BAUD_RATE = 9600

HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 12345

try:
    # Set up serial communication with Arduino
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to Arduino on {SERIAL_PORT}.")

    # Set up the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("Waiting for a client to connect...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        data = conn.recv(1024).decode().strip()  # Receive data from the client
        if data:
            print(f"Received: {data}")
            arduino.write(data.encode())  # Send the message to the Arduino

except KeyboardInterrupt:
    print("\nShutting down.")
    conn.close()
    server_socket.close()
    arduino.close()
except Exception as e:
    print(f"Error: {e}")

