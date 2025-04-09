import socket
import pygame  # Requires 'pip install pygame'
import time
import paramiko  # Require 'pip install paramiko'
#import subprocess  # Used for opening a new terminal window
import threading  # For running the log display in a separate thread
import re
import os
from dotenv import load_dotenv, find_dotenv # pip install python-dotenv

# Define Jetson Orin Nano's IP and port
PORT = 12345  # Port number (should match the Jetson server)

# Initialize pygame and the joystick
pygame.init()
pygame.joystick.init()
os.system('cls')

# Ensure at least one controller is connected
# if pygame.joystick.get_count() == 0:
#     print("No controller detected. Please connect an Xbox controller and restart.")
#     exit()
# joystick = pygame.joystick.Joystick(0)
# joystick.init()

# Create a socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Variable to track the last time a command was sent
last_time = time.time()
command_sent = ""

# Function to capture and display Jetson logs via SSH
def display_jetson_log(JETSON_IP, JETSON_USER, JETSON_PASS):
    try:
        # SSH client setup to read the log file remotely
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically accept the host key
        ssh_client.connect(JETSON_IP, username=JETSON_USER, password=JETSON_PASS)

        # Open the log file remotely on the Jetson and "tail -f" it
        command = f"tail -f ~/CodeWorkspace/UGV-Robot/Main/jetson_server_output.log"
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Regular expression to remove the INFO:root: part
        log_prefix_pattern = r"^[A-Z]+:[a-z]+:"  # Matches strings like INFO:root:

        # Continuously read from the SSH output (tail -f) and display it in the laptop terminal
        while True:
            output = stdout.readline()
            if output == '' and stdout.channel.exit_status_ready():
                break
            if output:
                # Clean up the log output by removing the INFO:root: part using regular expression
                cleaned_output = re.sub(log_prefix_pattern, '', output.strip())
                print(f"{cleaned_output}")

        ssh_client.close()

    except Exception as e:
        print(f"Error while displaying the log: {e}")
    except KeyboardInterrupt:
        pass

# Function to capture the local terminal output (laptop's terminal)
def capture_local_terminal():
    global last_time, command_sent
    try:
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
                        print(f"Client: {new_command}")
                        command_sent = new_command
                        last_time = current_time  # Update last_time

            # Check if the "Back" button (button B) is pressed to exit.
            if joystick.get_button(1):
                new_command = "exit"
                client_socket.sendall(new_command.encode())
                break

            time.sleep(0.02)  # Small delay to prevent excessive CPU usage

    except KeyboardInterrupt:
        new_command = "exit"
        client_socket.sendall(new_command.encode())
        pass

# Function to start a new terminal window on the laptop to show Jetson's terminal output
def start_jetson_server(JETSON_IP, JETSON_USER, JETSON_PASS):
    try:
        # SSH client setup to run the jetson_server.py remotely
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically accept the host key

        # Connect to Jetson Nano
        ssh_client.connect(JETSON_IP, username=JETSON_USER, password=JETSON_PASS)

        # Start the jetson_server.py script in the background
        command = f'python3 ~/CodeWorkspace/UGV-Robot/Main/jetson_server.py &'
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print("Started jetson_server.py on the Jetson.")
        ssh_client.close()

    except Exception as e:
        print(f"Error starting the Jetson server: {e}")

# Wait for Jetson server to be ready for connection
def wait_for_jetson_server(JETSON_IP):
    while True:
        try:
            # Attempt to connect to the Jetson Nano's socket
            client_socket.connect((JETSON_IP, PORT))
            print("Successfully connected to Jetson server.")
            break  # Exit the loop if the connection is successful
        except (socket.error, ConnectionRefusedError) as e:
            print("Waiting for Jetson server to be ready...")
            time.sleep(2)  # Wait for 2 seconds before retrying

def type_in_Jetson_connection_info():
    # Try to find and load the .env file
    dotenv_path = find_dotenv()

    if dotenv_path:
        load_dotenv(dotenv_path)
        print(".env file found.")
        JETSON_IP = os.getenv("IP_ADDRESS")
        JETSON_USER = os.getenv("JETSON_USER")
        JETSON_PASS = os.getenv("JETSON_PASS")

    else:
        print(".env file does not exist.")
        JETSON_IP = input("Type the IP address of the Jetson: ") # Jetson IP address
        JETSON_USER = input("Type the username of the Jetson account: ")  # Jetson Username
        JETSON_PASS = input("Type the password of the Jetson account: ")  # Jetson Password
    return JETSON_IP, JETSON_USER, JETSON_PASS


# Start the local terminal capture and the Jetson terminal capture
if __name__ == "__main__":
    JETSON_IP, JETSON_USER, JETSON_PASS = type_in_Jetson_connection_info()
    start_jetson_server(JETSON_IP, JETSON_USER, JETSON_PASS) 
    wait_for_jetson_server(JETSON_IP)

    # Start the display_log function in a separate thread
    log_thread = threading.Thread(target=display_jetson_log, args=(JETSON_IP, JETSON_USER, JETSON_PASS))
    log_thread.start()

    capture_local_terminal()

    # Close the socket and quit pygame
    client_socket.close()
    pygame.quit()
    print("Client: Connection closed.")
    os._exit(1)