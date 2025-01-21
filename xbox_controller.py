# pip install pygame inputs
# Xbox controller python code. Working.
import pygame

# Initialize Pygame's joystick module
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick connected!")
    pygame.quit()
    exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Using joystick: {joystick.get_name()}")

try:
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} moved to {event.value:.2f}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    pygame.quit()
