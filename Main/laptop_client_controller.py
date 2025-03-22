import socket
import pygame  # Requires 'pip install pygame'
import time
import paramiko  # Require 'pip install paramiko'
import subprocess  # Used for opening a new terminal window

# Define Jetson Orin Nano's IP and port
JETSON_IP = "10.0.0.179"  # Replace with the Jetson's actual IP address
JETSON_USER = "ugv-c7"     # Jetson Username
JETSON_PASS = "stevens-siemens-C7"  # Jetson Password
PORT = 12345  # Port number (should match the Jetson server)

# Initialize pygame and the joystick
pygame.init()
pygame.joystick.init()

# Ensure at least one controller is connected
if pygame.joystick.get_count() == 0:
    print("No controller detected. Please connect an Xbox controller and restart.")
    exit()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Create a socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Variable to track the last time a command was sent
last_time = time.time()
command_sent = ""

# Function to capture the Jetson Nano's terminal output through SSH
def capture_jetson_terminal():
    try:
        # SSH client setup
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically accept the host key

        # Connect to Jetson Nano
        ssh_client.connect(JETSON_IP, username=JETSON_USER, password=JETSON_PASS)

        # Open an interactive shell session
        stdin, stdout, stderr = ssh_client.exec_command('/bin/bash')

        # Continuously read and print output from the Jetson Nano
        while True:
            output = stdout.readline()
            if output == '' and stdout.channel.exit_status_ready():
                break
            if output:
                print(f"Jetson Terminal: {output}", end='')  # Print Jetson's output

        ssh_client.close()
    except Exception as e:
        print(f"Error capturing Jetson terminal: {e}")

# Function to capture the local terminal output (laptop's terminal)
def capture_local_terminal():
    global last_time, command_sent
    try:
        print("Use the left joystick to send commands. Press 'Back' on the controller to exit.")

        while True:
            pygame.event.pump()  # Process controller events
            current_time = time.time()

            right_trigger = joystick.get_axis(3)

            # Only send commands if the right trigger is pressed (threshold check)
            if right_trigger > 0.5:
                # Process input every 0.5 seconds
                if current_time - last_time >= 0.5:
                    x_axis = joystick.get_axis(0)  # Left joystick horizontal (-1 to 1)
                    y_axis = joystick.get_axis(1)  # Left joystick vertical (-1 to 1)

                    if y_axis < -0.5:  # Move up
                        new_command = "UP"
                    elif y_axis > 0.5:  # Move down
                        new_command = "DOWN"
                    elif x_axis < -0.5:  # Move left
                        new_command = "LEFT"
                    elif x_axis > 0.5:  # Move right
                        new_command = "RIGHT"
                    else:
                        new_command = ""

                    # Send the command if it has changed
                    if new_command and new_command != command_sent:
                        client_socket.sendall(new_command.encode())
                        print(f"Local Terminal Command Sent: {new_command}")
                        command_sent = new_command
                        last_time = current_time  # Update last_time

            # Check if the "Back" button (button B) is pressed to exit.
            if joystick.get_button(1):
                break

            time.sleep(0.01)  # Small delay to prevent excessive CPU usage

    except KeyboardInterrupt:
        pass

# Function to start a new terminal window on the laptop to show Jetson's terminal output
def start_laptop_terminal():
    try:
        # Launch a new terminal window on the laptop to show the Jetson's terminal output
        # We'll use gnome-terminal for Linux. You could change this to xterm, etc., if needed
        command = f'gnome-terminal -- bash -c "python3 {__file__}; exec bash"'
        subprocess.Popen(command, shell=True)
        print("Opened a new terminal window on the laptop.")
    except Exception as e:
        print(f"Error opening new terminal window: {e}")

# Wait for Jetson server to be ready for connection
def wait_for_jetson_server():
    while True:
        try:
            # Attempt to connect to the Jetson Nano's socket
            client_socket.connect((JETSON_IP, PORT))
            print("Successfully connected to Jetson server.")
            break  # Exit the loop if the connection is successful
        except (socket.error, ConnectionRefusedError) as e:
            print("Waiting for Jetson server to be ready...")
            time.sleep(2)  # Wait for 2 seconds before retrying

# Start the Jetson server
start_laptop_terminal()  # Start the terminal window for showing Jetson terminal

# Wait for the Jetson server to be ready to accept connections
wait_for_jetson_server()

# Start the local terminal capture and the Jetson terminal capture
if __name__ == "__main__":
    capture_local_terminal()

    # Close the socket and quit pygame
    client_socket.close()
    pygame.quit()
    print("Connection closed.")