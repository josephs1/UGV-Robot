import serial
import time

# Set up serial connection to Arduino
SERIAL_PORT = "/dev/ttyACM0"  # Change this if necessary
BAUD_RATE = 9600
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

try:
    # Define messages to send
    messages = ["UP", "DOWN", "LEFT", "RIGHT"]
    
    for msg in messages:
        print(f"Sending message to Arduino: {msg}")
        arduino.write(f"{msg}\n".encode())  # Send message to Arduino
        time.sleep(1)  # Wait for Arduino to process and respond

        # Read the response from Arduino
        response = arduino.readline().decode("utf-8").strip()
        print(f"Received from Arduino: {response}")
finally:
    arduino.close()
    print("Serial connection closed.")
