import serial
import pygame
import time
import os

# Set up serial connection to Arduino
SERIAL_PORT = "/dev/ttyACM0"  # Replace with the Arduino's serial port
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

def main():
    try:
        while True:
            pygame.event.pump()  # Process controller events
            if not motorPicked:
                print("Please pick a motor to control.")
                print("Press X to control a servo motor.")
                print("Press Y to control a drivetrain motor.")
                while not motorPicked:
                    if joystick.get_button(2):
                        motorType = 1
                        servoPos = 0
                        print("Servo motor selected.")
                        cmd = "servo"
                        arduino.write(cmd.encode())
                        motorPicked = True
                    elif joystick.get_button(3):
                        motorType = 2
                        motorSpeed = 0
                        print("Drivetrain motor selected.")
                        cmd = "motor"
                        arduino.write(cmd.encode())
                        motorPicked = True
            else:
                right_trigger = joystick.get_axis(3)
                if right_trigger > 0.5:
                    x_axis = joystick.get_axis(0)  # Left joystick horizontal (-1 to 1)
                    if motorType == 1:
                        if x_axis < -0.5:  # Move servo left
                            if servoPos > 0:
                                servoPos -= 1
                                print(f"Servo Position: {servoPos}")
                                cmd = str(servoPos)
                                arduino.write(cmd.encode())
                        elif x_axis > 0.5:  # Move right
                            if servoPos < 270:
                                servoPos += 1
                                print(f"Servo Position: {servoPos}")
                                cmd = str(servoPos)
                                arduino.write(cmd.encode())
                        else:
                            cmd = ""
                            arduino.write(cmd.encode())
                    elif motorType == 2:
                        if x_axis < -0.5:  # Move servo left
                            if motorSpeed > -1.0:
                                motorSpeed -= 0.05
                                print(f"Motor Speed: {motorSpeed}")
                                cmd = str(motorSpeed)
                                arduino.write(cmd.encode())
                        elif x_axis > 0.5:  # Move right
                            if motorSpeed < 1.0:
                                servoPos += 0.05
                                print(f"Motor Speed: {motorSpeed}")
                                cmd = str(motorSpeed)
                                arduino.write(cmd.encode())
                        else:
                            cmd = ""
                            arduino.write(cmd.encode())

            # B button to select motor type
            if joystick.get_button(1):
                if motorPicked == True:
                    cmd = "selection"
                    arduino.write(cmd.encode())
                    motorPicked = False
                else:
                    break

            time.sleep(0.15)  # Small delay to prevent excessive CPU usage

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
    pygame.quit()
    arduino.close()
    print("Connection closed.")
    os._exit(1)