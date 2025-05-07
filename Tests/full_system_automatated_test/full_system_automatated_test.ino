#include <Servo.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// Servo Info
#define MIN_PULSE_WIDTH 500 // Servo Min Pulse Width
#define MAX_PULSE_WIDTH 2500 // Servo Max Pulse Width
#define FREQUENCY 50 // Frequency for PCA9685
#define servo1 0 // Servo Channel 1
#define servo2 4 // Servo Channel 5
#define servo3 8 // Servo Channel 9

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Motor Pins
#define LEFT_MOTOR_1 8  
#define LEFT_MOTOR_2 9 
#define RIGHT_MOTOR_1 7  
#define RIGHT_MOTOR_2 6

// Nema Stepper Motor Pins & Info
const int dirPin = 3;    // Direction pin (DIR+)
const int stepPin = 2;   // Step pin (PUL+)
const int microstepping = 8; // Might need to change to 32.
const int stepsPerRevolution = 200 * microstepping; // Full steps (1.8° per step)
const float degreesPerStep = 360.0 / stepsPerRevolution; // = 1.8 if no microstepping

float currentAngle = 0.0;    // Track current position
float targetAngle = 0.0;
unsigned long lastStepTime = 0;
const unsigned long stepDelay = 1500;

// Spark MAX Motor Controllers
Servo left_wheel_motor1; 
Servo left_wheel_motor2;
Servo right_wheel_motor1; 
Servo right_wheel_motor2; 

void setup() {
    pinMode(stepPin, OUTPUT);
    pinMode(dirPin, OUTPUT);
    pwm.begin();
    pwm.setPWMFreq(FREQUENCY);
    Serial.begin(9600); // Start serial communication
    Serial.flush();
    left_wheel_motor1.attach(LEFT_MOTOR_1);
    left_wheel_motor2.attach(LEFT_MOTOR_2);    
    right_wheel_motor1.attach(RIGHT_MOTOR_1);
    right_wheel_motor2.attach(RIGHT_MOTOR_2);
    stopMotors();
    moveServo(servo1, servoPos1);
    moveServo(servo2, servoPos2);
    moveServo(servo3, servoPos3);
}
  
void loop() {
    float directionValue = args.toFloat();
    const float stepAngle = 20.0;  // Step in 20-degree increments
    // Update target angle based on input
    if (directionValue == 1.0) {
        targetAngle += stepAngle;  // Increase by 20 degrees
    } else if (directionValue == -1.0) {
        targetAngle -= stepAngle;  // Decrease by 20 degrees
    }

    // Clamp angle between -3600 and 3600 (i.e. 180 * 20)
    if (targetAngle > 3600) targetAngle = 3600;
    if (targetAngle < -3600) targetAngle = -3600;

    moveStepperToTarget();
    moveServo(servo1, servoPos1);
    moveServo(servo2, servoPos2);
    moveServo(servo3, servoPos3);
    left_wheel_motor1.writeMicroseconds(speedToPulseWidth(speed));
    left_wheel_motor2.writeMicroseconds(speedToPulseWidth(speed));
    right_wheel_motor1.writeMicroseconds(speedToPulseWidth(speed));
    right_wheel_motor2.writeMicroseconds(speedToPulseWidth(speed));
    delay(20);
}

void stopMotors() {
    left_wheel_motor1.writeMicroseconds(speedToPulseWidth(0));
    left_wheel_motor2.writeMicroseconds(speedToPulseWidth(0));
    right_wheel_motor1.writeMicroseconds(speedToPulseWidth(0));
    right_wheel_motor2.writeMicroseconds(speedToPulseWidth(0));
}
  
// Function to map speed (-1.0 to 1.0) to PWM pulse width (1000 to 2000 μs)
int speedToPulseWidth(float speed) {
    speed = constrain(speed, -0.5, 0.5); // Ensure speed is within range (-0.6, 0.6). Change later to (-1.0, 1.0).

    // Map the speed to a pulse width between 1000 and 2000 μs
    return map(speed * 100, -100, 100, 1000, 2000); // Return pulse width in microseconds
}

void moveServo(int servoOut, int angle){
   int pulseWidth = map(angle, 0, 270, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);

   // Convert the pulse width to a value suitable for the PCA9685
   int pulseValue = int(float(pulseWidth) / 1000000 * FREQUENCY * 4096);
   pwm.setPWM(servoOut, 0, pulseValue);
}

void moveStepperToTarget() {
    float angleDiff = targetAngle - currentAngle;
    int direction = (angleDiff >= 0) ? HIGH : LOW;
    int stepsToMove = abs(angleDiff) / degreesPerStep;

    digitalWrite(dirPin, direction);

    static unsigned long lastStepTime = 0; // Track time between steps
    const unsigned long stepInterval = 1500; // Microseconds per step

    for (int i = 0; i < stepsToMove; i++) {
        while (micros() - lastStepTime < stepInterval) {
            // Wait without blocking the rest of the code
        }
        lastStepTime = micros();
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(2); // Short pulse for step
        digitalWrite(stepPin, LOW);
    }

    currentAngle = targetAngle;
    Serial.print("Moved to angle: ");
    Serial.println(currentAngle);
}
