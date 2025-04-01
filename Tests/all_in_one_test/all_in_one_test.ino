#include <Servo.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define MOTOR_PWM_PIN 9  // PWM Output Pin for Motor Controller
#define MIN_PULSE_WIDTH 500 // Servo Min Pulse Width
#define MAX_PULSE_WIDTH 2500 // Servo Max Pulse Width
#define FREQUENCY 50 // Frequency for PCA9685
#define servo1 0 // Servo Channel 1

Servo motorController; // Spark MAX Motor Controller
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

int motorType = 0;
float motorSpeed = 0.0;
int servoPos = 0;

void setup() {
    motorController.attach(MOTOR_PWM_PIN);
    pwm.begin();
    pwm.setPWMFreq(FREQUENCY);
    Serial.begin(9600);   // Initialize serial communication
    pinMode(13, OUTPUT);  // Set the built-in LED on pin 13 as an output
  }
  
void loop() {
    if (Serial.available() > 0) { // Changed from if to while. Might need to change back.
        byte cmd = Serial.read();

        if (cmd == 1) {
            motorType = 1;
        } 
        else if (cmd == 2){
            motorType = 2;
        }
        else if (cmd == 0){
            if (motorType == 1){
                moveServo(servo1, 0);
                servoPos = 0;
            }
            else if (motorType == 2){
                motorController.writeMicroseconds(speedToPulseWidth(0.0)); // Send PWM signal
                motorSpeed = 0.0;
            }
        }
        else if (cmd == 3){
            if (motorType == 1){
                if (servoPos < 270){
                  servoPos += 7;
                }
                moveServo(servo1, servoPos);
            }
            else if (motorType == 2){
                if (motorSpeed < 0.6){ // Change later to 1.0
                  motorSpeed += 0.025;
                }
                motorController.writeMicroseconds(speedToPulseWidth(motorSpeed)); // Send PWM signal
            }
        }
        else if (cmd == 4){
            if (motorType == 1){
                if (servoPos > 0){
                  servoPos -= 7;
                }
                moveServo(servo1, servoPos);
            }
            else if (motorType == 2){
                if (motorSpeed > -0.6){ // Change later to -1.0
                  motorSpeed -= 0.025;
                }
                motorController.writeMicroseconds(speedToPulseWidth(motorSpeed)); // Send PWM signal
            }
        }
    }
    delay(50);
}
  
// Function to map speed (-1.0 to 1.0) to PWM pulse width (1000 to 2000 μs)
int speedToPulseWidth(float speed) {
    speed = constrain(speed, -0.6, 0.6); // Ensure speed is within range (-0.6, 0.6). Change later to (-1.0, 1.0).

    // Map the speed to a pulse width between 1000 and 2000 μs
    return map(speed * 100, -100, 100, 1000, 2000); // Return pulse width in microseconds
}

void moveServo(int servoOut, int angle){
    int pulseWidth = map(angle, 0, 270, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);

    // Convert the pulse width to a value suitable for the PCA9685
    int pulseValue = int(float(pulseWidth) / 1000000 * FREQUENCY * 4096);
    pwm.setPWM(servoOut, 0, pulseValue);
  }
