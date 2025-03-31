import pygame
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected. Please connect an Xbox controller and restart.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Joystick detected: {joystick.get_name()}")

try:
    while True:
        pygame.event.pump()  # Process input events
        for i in range(joystick.get_numaxes()):
            value = joystick.get_axis(i)
            print(f"Axis {i}: {value:.2f}")
        print("-" * 30)
        time.sleep(0.15)
except KeyboardInterrupt:
    pygame.quit()
