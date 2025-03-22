# Used sudo apt install python3-serial on jetson
import socket
import serial
import logging

# Set up serial connection to Arduino
########SERIAL_PORT = "/dev/ttyACM0"  # Replace with the Arduino's serial port
# Command for scanning ports: ls /dev/ttyACM*
# Giving write permissions: sudo chmod 666 /dev/ttyACM0
BAUD_RATE = 9600
########arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Set up server
HOST = "0.0.0.0"
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

client_socket, addr = server_socket.accept()
# Set up logging
logging.basicConfig(filename='/home/ugv-c7/CodeWorkspace/UGV-Robot/Main/jetson_server_output.log', level=logging.INFO)

logging.info("Waiting for connection from laptop...")

logging.info(f"Connected to {addr}")

try:
    while True:
        # Receive data from laptop
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        logging.info(f"Received from laptop: {data}")
        
        # Send data to Arduino
        ##########arduino.write(data.encode())
except Exception as e:
    logging.error(f"Error occurred: {e}")
finally:
    client_socket.close()
    ##########arduino.close()
    logging.info("Connections closed.")
