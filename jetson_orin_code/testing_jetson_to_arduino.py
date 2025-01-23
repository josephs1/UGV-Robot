import serial
import time

# Serial port and baud rate configuration
SERIAL_PORT = "/dev/ttyACM0"  # Update this if your Arduino is on a different port
BAUD_RATE = 9600

try:
    # Establish serial connection
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Wait for the connection to initialize

    # Message to send
    message = "Hello, Arduino!"
    print(f"Sending message: {message}")
    arduino.write((message + '\n').encode())  # Send message with a newline character

    # Optional: Read response from Arduino (if any)
    response = arduino.readline().decode().strip()
    if response:
        print(f"Response from Arduino: {response}")

finally:
    # Close the connection
    arduino.close()
    print("Serial connection closed.")
