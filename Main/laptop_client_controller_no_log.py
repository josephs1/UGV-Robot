import socket
import pygame  # Requires 'pip install pygame'
import time
import paramiko  # Require 'pip install paramiko'
#import subprocess  # Used for opening a new terminal window
#import threading  # For running the log display in a separate thread
#import re
import os
from dotenv import load_dotenv, find_dotenv # pip install python-dotenv

# Define Jetson Orin Nano's IP and port
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
    PORT = int(os.getenv("PORT"))
else:
    PORT = 12345  # Port number (should match the Jetson server)

# Initialize pygame and the joystick
pygame.init()
pygame.joystick.init()
os.system('cls')

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
previous_command = ""

# --- Commented out: Jetson log display functionality ---
# def display_jetson_log(JETSON_IP, JETSON_USER, JETSON_PASS):
#     try:
#         ssh_client = paramiko.SSHClient()
#         ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh_client.connect(JETSON_IP, username=JETSON_USER, password=JETSON_PASS)
#         command = f"tail -f ~/CodeWorkspace/UGV-Robot/Main/jetson_server_output.log"
#         stdin, stdout, stderr = ssh_client.exec_command(command)
#         log_prefix_pattern = r"^[A-Z]+:[a-z]+:"
#         while True:
#             output = stdout.readline()
#             if output == '' and stdout.channel.exit_status_ready():
#                 break
#             if output:
#                 cleaned_output = re.sub(log_prefix_pattern, '', output.strip())
#                 print(f"{cleaned_output}")
#         ssh_client.close()
#     except Exception as e:
#         print(f"Error while displaying the log: {e}")
#     except KeyboardInterrupt:
#         pass

def capture_local_terminal():
    global last_time, previous_command
    active_device = "servo1"
    devices = ["servo1", "servo2", "servo3", "nema"]
    device_index = 0
    x_button_prev = 0
    try:
        while True:
            pygame.event.pump()
            current_time = time.time()
            right_trigger = joystick.get_axis(5)
            x_button = joystick.get_button(2)

            if x_button and not x_button_prev and right_trigger <= 0.5:
                device_index = (device_index + 1) % len(devices)
                active_device = devices[device_index]
                print(f"Switched control to: {active_device}")

            x_button_prev = x_button

            if right_trigger <= 0.5:
                if current_time - last_time >= 0.2:
                    right_y_axis = joystick.get_axis(3)
                    deadzone = 0.25
                    if abs(right_y_axis) > deadzone:
                        value = -1.0 if right_y_axis > 0 else 1.0
                        command = f"{active_device},{value:.1f}\n"
                        client_socket.sendall(command.encode())
                        print(f"Client: {active_device} → {value:.1f}")
                        last_time = current_time
                        if active_device == "nema":
                            time.sleep(0.01)
                    else:
                        value = 0.0

            elif right_trigger > 0.5:
                if current_time - last_time > 0.2:
                    left_y_axis = joystick.get_axis(1)
                    right_y_axis = joystick.get_axis(3)
                    if abs(left_y_axis) < 0.1:
                        left_y_axis = 0.0
                    if abs(right_y_axis) < 0.1:
                        right_y_axis = 0.0
                    command = f"drive,{left_y_axis:.2f},{right_y_axis:.2f}\n"
                    if command != previous_command:
                        client_socket.sendall(command.encode())
                        print(f"Client: Drive command sent - Left: {left_y_axis:.2f}, Right: {right_y_axis:.2f}")
                        previous_command = command
                        last_time = current_time

            if joystick.get_button(1):
                new_command = "exit"
                client_socket.sendall(new_command.encode())
                break

            time.sleep(0.1)

    except KeyboardInterrupt:
        new_command = "exit"
        client_socket.sendall(new_command.encode())
        pass

def start_jetson_server(JETSON_IP, JETSON_USER, JETSON_PASS):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(JETSON_IP, username=JETSON_USER, password=JETSON_PASS)
        command = f'python3 ~/CodeWorkspace/UGV-Robot/Main/jetson_server_no_log.py &'
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print("Started jetson_server.py on the Jetson.")
        ssh_client.close()
    except Exception as e:
        print(f"Error starting the Jetson server: {e}")

def wait_for_jetson_server(JETSON_IP):
    while True:
        try:
            client_socket.connect((JETSON_IP, PORT))
            print("Successfully connected to Jetson server.")
            break
        except (socket.error, ConnectionRefusedError):
            print("Waiting for Jetson server to be ready...")
            time.sleep(2)

def type_in_Jetson_connection_info():
    dotenv_path = find_dotenv()
    if dotenv_path:
        load_dotenv(dotenv_path)
        print(".env file found.")
        JETSON_IP = os.getenv("JETSON_IP")
        JETSON_USER = os.getenv("JETSON_USER")
        JETSON_PASS = os.getenv("JETSON_PASS")
    else:
        print(".env file does not exist.")
        JETSON_IP = input("Type the IP address of the Jetson: ")
        JETSON_USER = input("Type the username of the Jetson account: ")
        JETSON_PASS = input("Type the password of the Jetson account: ")
    return JETSON_IP, JETSON_USER, JETSON_PASS

if __name__ == "__main__":
    JETSON_IP, JETSON_USER, JETSON_PASS = type_in_Jetson_connection_info()
    start_jetson_server(JETSON_IP, JETSON_USER, JETSON_PASS)
    wait_for_jetson_server(JETSON_IP)

    # --- Commented out: starting Jetson log thread ---
    # log_thread = threading.Thread(target=display_jetson_log, args=(JETSON_IP, JETSON_USER, JETSON_PASS))
    # log_thread.start()

    capture_local_terminal()

    client_socket.close()
    pygame.quit()
    print("Client: Connection closed.")
    os._exit(1)
