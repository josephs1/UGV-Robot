import serial
import time

# Configure the serial connection to the Arduino (Make sure to use your correct COM port)
arduino = serial.Serial('COM6', 9600, timeout=1)  # Replace 'COM3' with your Arduino port
time.sleep(2)  # Give the Arduino some time to reset

# Send "ON" message to Arduino
arduino.write(b"ON\n")  # Send ON to turn on the LED
print("Sent: ON")
time.sleep(2)  # Wait for 2 seconds

# Send "OFF" message to Arduino
arduino.write(b"OFF\n")  # Send OFF to turn off the LED
print("Sent: OFF")

# Close the serial connection
arduino.close()
