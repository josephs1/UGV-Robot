import serial
import pygame
import time
import os

# Set up serial connection to Arduino
SERIAL_PORT = "COM6" #"/dev/ttyACM0"  # Replace with the Arduino's serial port
# Command for scanning ports: ls /dev/ttyACM*
# Giving write permissions: sudo chmod 666 /dev/ttyACM0
BAUD_RATE = 9600
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

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

motorPicked = False
motorType = None
servoPos = 0
motorSpeed = 0.00

def main():
    global motorPicked
    global motorType
    global servoPos
    global motorSpeed
    try:
        while True:
            if not motorPicked:
                print("Please pick a motor to control.")
                print("Press X to control a servo motor.")
                print("Press Y to control a drivetrain motor.")
                while not motorPicked:
                    pygame.event.pump()  # Process controller events
                    if joystick.get_button(2):
                        motorType = 1
                        servoPos = 0
                        print("Servo motor selected.")
                        cmd = bytes([1])
                        arduino.write(cmd)
                        motorPicked = True
                    elif joystick.get_button(3):
                        motorType = 2
                        motorSpeed = 0
                        print("Drivetrain motor selected.")
                        cmd = bytes([2])
                        arduino.write(cmd)
                        motorPicked = True
                    elif joystick.get_button(1):
                        # Stop the motor/servo
                        cmd = bytes([0])
                        arduino.write(cmd)

                        # Close the serial connection and quit pygame.
                        pygame.quit()
                        arduino.close()
                        print("Connection closed.")
                        os._exit(1)
            else:
                pygame.event.pump()  # Process controller events
                right_trigger = joystick.get_axis(5) # Right Trigger
                if right_trigger > 0.5:
                    x_axis = joystick.get_axis(0)  # Left joystick horizontal (-1 to 1)
                    if motorType == 1:
                        if x_axis > 0.5:  # Move right
                            if (servoPos < 270):
                                servoPos += 7
                            print(f"Servo Position: {servoPos}")
                            cmd = bytes([3])
                            arduino.write(cmd)
                        elif x_axis < -0.5:
                            if (servoPos > 0):
                                servoPos -= 7
                            print(f"Servo Position: {servoPos}")
                            cmd = bytes([4])
                            arduino.write(cmd)
                    elif motorType == 2:
                        if x_axis > 0.5:  # Move right
                            if (motorSpeed < 0.6): # Change later to 1.0
                                motorSpeed += 0.025
                                motorSpeed = round(motorSpeed, 3)
                            print(f"Motor Speed: {motorSpeed}")
                            cmd = bytes([3])
                            arduino.write(cmd)
                        elif x_axis < -0.5:  # Move servo left
                            if (motorSpeed > -0.6): # Change later to -1.0
                                motorSpeed -= 0.025
                                motorSpeed = round(motorSpeed, 3)
                            print(f"Motor Speed: {motorSpeed}")
                            cmd = bytes([4])
                            arduino.write(cmd)
                else:
                    if motorSpeed != 0.0:
                        cmd = bytes([0]) # Stop the motor/servo
                        arduino.write(cmd)
                        motorSpeed = 0.0
                    
            # B button to select motor type
            if joystick.get_button(1):
                cmd = bytes([0]) # Stop the motor/servo
                arduino.write(cmd)
                motorPicked = False

            time.sleep(0.07)  # Small delay to prevent excessive CPU usage. 250 Hz is 4 ms.

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

    # Stop the motor/servo
    cmd = bytes([0])
    arduino.write(cmd)

    # Close the serial connection and quit pygame.
    pygame.quit()
    arduino.close()
    print("Connection closed.")
    os._exit(1)