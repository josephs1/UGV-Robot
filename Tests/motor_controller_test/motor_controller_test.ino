#include <Servo.h>

#define MOTOR_PWM_PIN 9  // PWM Output Pin

Servo motorController; // Spark MAX Motor Controller

void setup() {
    motorController.attach(MOTOR_PWM_PIN);  
}

void loop() {
    float speed = 0.6; // Set speed
    speed = constrain(speed, -1.0, 1.0); // Ensure speed is within range
    
    int pulseWidth = mapSpeedToPWM(speed); // map speed to pulse width
    motorController.writeMicroseconds(pulseWidth); // Send PWM signal
    delay(1200); // delay (range of 5-20 ms)

    speed = 0; // Set speed
    speed = constrain(speed, -1.0, 1.0); // Ensure speed is within range
    
    pulseWidth = mapSpeedToPWM(speed); // map speed to pulse width
    motorController.writeMicroseconds(pulseWidth); // Send PWM signal
    delay(1200); // delay (range of 5-20 ms)

    speed = -0.6; // Set speed
    speed = constrain(speed, -1.0, 1.0); // Ensure speed is within range
    
    pulseWidth = mapSpeedToPWM(speed); // map speed to pulse width
    motorController.writeMicroseconds(pulseWidth); // Send PWM signal
    delay(1200); // delay (range of 5-20 ms)
//    motorController.writeMicroseconds(1300);
//    delay(1200);
//    motorController.writeMicroseconds(1700);
//    delay(1200);
}

// Function to map speed (-1.0 to 1.0) to PWM pulse width (1000 to 2000 μs)
int mapSpeedToPWM(float speed) {
    return map(speed * 100, -100, 100, 1000, 2000);
}
