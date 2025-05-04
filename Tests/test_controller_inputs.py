import pygame
import sys

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick controller detected.")
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

try:
    while True:
        pygame.event.pump()
        axis_values = {}
        for i in range(joystick.get_numaxes()):
            axis_values[f"Axis {i}"] = joystick.get_axis(i)

        print("\033c", end="")
        for name, value in axis_values.items():
            print(f"{name}: {value:.3f}")

        pygame.time.wait(100)
except KeyboardInterrupt:
    print("Aww man")
finally:
    pygame.exit()