# Xbox controller for Python. Working.
# For simpler input handling, you can use the inputs library:
"""
Controller Testing: Test your controller using software like jstest (Linux) or the
Game Controllers tool (Windows)to ensure it's working before running the script
"""
from inputs import get_gamepad

try:
    print("Listening to the Xbox controller...")
    while True:
        events = get_gamepad()
        for event in events:
            print(f"Event: {event.ev_type}, Code: {event.code}, State: {event.state}")

except KeyboardInterrupt:
    print("\nExiting...")
