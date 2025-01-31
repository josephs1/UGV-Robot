import socket
import pygame  # Requires `pip install pygame`
import time

# Define Jetson Orin Nano's IP and port
JETSON_IP = "192.168.1.189"  # Replace with the Jetson's actual IP address
PORT = 12345

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
client_socket.connect((JETSON_IP, PORT))

# Variable to track the last time a command was sent
last_time = time.time()
command_sent = ""

try:
    print("Use the left joystick to send commands. Press 'Back' on the controller to exit.")
    
    while True:
        pygame.event.pump()  # Process controller events
        current_time = time.time()
        
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

            # Send the command if it has changed. (Would get rid of in actual or maybe just have it so when new commend="" is sent, to update)
            if new_command and new_command != command_sent:
                client_socket.sendall(new_command.encode())
                print(f"Sent: {new_command}")
                command_sent = new_command
                last_time = current_time  # Update last_time

            # Check if the "Back" button (button B) is pressed to exit. (0 is A button. 1 is B button.)
            if joystick.get_button(1):
                break

        time.sleep(0.01)  # Small delay to prevent excessive CPU usage

except KeyboardInterrupt:
    pass
finally:
    client_socket.close()
    print("Connection closed.")
    pygame.quit()
