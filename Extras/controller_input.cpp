// C++ code for xbox controller. Doesn't work.
#include <iostream>
#include <Windows.h>
#include <Xinput.h>

// Link to XInput library
#pragma comment(lib, "xinput.lib")

void PrintControllerState(const XINPUT_STATE& state) {
    std::cout << "Buttons Pressed: ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_A) std::cout << "A ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_B) std::cout << "B ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_X) std::cout << "X ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_Y) std::cout << "Y ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_DPAD_UP) std::cout << "DPad Up ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_DPAD_DOWN) std::cout << "DPad Down ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_DPAD_LEFT) std::cout << "DPad Left ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_DPAD_RIGHT) std::cout << "DPad Right ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_LEFT_SHOULDER) std::cout << "Left Shoulder ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_RIGHT_SHOULDER) std::cout << "Right Shoulder ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_START) std::cout << "Start ";
    if (state.Gamepad.wButtons & XINPUT_GAMEPAD_BACK) std::cout << "Back ";
    std::cout << "\n";

    std::cout << "Left Thumbstick: (" 
              << state.Gamepad.sThumbLX << ", " 
              << state.Gamepad.sThumbLY << ")\n";
    std::cout << "Right Thumbstick: (" 
              << state.Gamepad.sThumbRX << ", " 
              << state.Gamepad.sThumbRY << ")\n";
    std::cout << "Left Trigger: " 
              << static_cast<int>(state.Gamepad.bLeftTrigger) << "\n";
    std::cout << "Right Trigger: " 
              << static_cast<int>(state.Gamepad.bRightTrigger) << "\n";
}

int main() {
    XINPUT_STATE state;
    DWORD dwResult;

    std::cout << "Xbox Controller Input Test\n";

    while (true) {
        // Check the state of controller 0 (you can loop through controllers 0-3 for multiple controllers)
        dwResult = XInputGetState(0, &state);

        if (dwResult == ERROR_SUCCESS) {
            // Controller is connected
            PrintControllerState(state);
        } else {
            // Controller is not connected
            std::cout << "Controller not connected\n";
        }

        // Wait for a short time before polling again
        Sleep(100);
    }

    return 0;
}
