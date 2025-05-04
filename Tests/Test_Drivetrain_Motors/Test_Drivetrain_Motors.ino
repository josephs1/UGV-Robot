#include <Servo.h>
// #include <Wire.h>
// #include <Adafruit_PWMServoDriver.h>

// Motor Pins
#define LEFT_MOTOR_1 8  
#define LEFT_MOTOR_2 9 
#define RIGHT_MOTOR_1 7  
#define RIGHT_MOTOR_2 6

// Timer Variables
unsigned long lastDataTime = 0; // Track last time data was received
const unsigned long timeoutDuration = 2000; // 2-second timeout

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

// Servo Control Info
// #define MIN_PULSE_WIDTH 500 // Servo Min Pulse Width
// #define MAX_PULSE_WIDTH 2500 // Servo Max Pulse Width
// #define FREQUENCY 50 // Frequency for PCA9685
// #define servo1 0 // Servo Channel 1

// Spark MAX Motor Controllers
Servo left_wheel_motor1; 
Servo left_wheel_motor2;
Servo right_wheel_motor1; 
Servo right_wheel_motor2; 

// Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

//int motorType = 0;
String inputString = "";
float left_wheel_speed = 0.0;
float right_wheel_speed = 0.0;
//int servoPos = 0;

void setup() {
    pinMode(stepPin, OUTPUT);
    pinMode(dirPin, OUTPUT);
    Serial.begin(9600); // Start serial communication
    Serial.flush();
    left_wheel_motor1.attach(LEFT_MOTOR_1);
    left_wheel_motor2.attach(LEFT_MOTOR_2);    
    right_wheel_motor1.attach(RIGHT_MOTOR_1);
    right_wheel_motor2.attach(RIGHT_MOTOR_2); 
    //pwm.begin();
    //pwm.setPWMFreq(FREQUENCY);
}
  
void loop() {
    delay(2000);
    left_wheel_motor1.writeMicroseconds(speedToPulseWidth(-0.2));
    left_wheel_motor2.writeMicroseconds(speedToPulseWidth(-0.2));
    //right_wheel_motor1.writeMicroseconds(speedToPulseWidth(0.2));
    //right_wheel_motor2.writeMicroseconds(speedToPulseWidth(0.2));

    delay(1000);
    stopMotors();

    delay(2000);
    left_wheel_motor1.writeMicroseconds(speedToPulseWidth(0.2));
    left_wheel_motor2.writeMicroseconds(speedToPulseWidth(0.2));
    //right_wheel_motor1.writeMicroseconds(speedToPulseWidth(-0.2));
    //right_wheel_motor2.writeMicroseconds(speedToPulseWidth(-0.2));

    delay(1000);
    stopMotors();

    delay(2000);
    left_wheel_motor1.writeMicroseconds(speedToPulseWidth(0.2));
    left_wheel_motor2.writeMicroseconds(speedToPulseWidth(0.2));
    //right_wheel_motor1.writeMicroseconds(speedToPulseWidth(0.2));
    //right_wheel_motor2.writeMicroseconds(speedToPulseWidth(0.2));

    delay(1000);
    stopMotors();

    delay(2000);
    left_wheel_motor1.writeMicroseconds(speedToPulseWidth(-0.2));
    left_wheel_motor2.writeMicroseconds(speedToPulseWidth(-0.2));
    //right_wheel_motor1.writeMicroseconds(speedToPulseWidth(-0.2));
    //right_wheel_motor2.writeMicroseconds(speedToPulseWidth(-0.2));

    delay(1000);
    stopMotors();
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

// void moveServo(int servoOut, int angle){
//     int pulseWidth = map(angle, 0, 270, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);

//     // Convert the pulse width to a value suitable for the PCA9685
//     int pulseValue = int(float(pulseWidth) / 1000000 * FREQUENCY * 4096);
//     pwm.setPWM(servoOut, 0, pulseValue);
// }

void moveStepperToTarget() {
    float angleDiff = targetAngle - currentAngle;
    int direction = (angleDiff >= 0) ? HIGH : LOW;
    int stepsToMove = abs(angleDiff) / degreesPerStep;

    // Ensure targetAngle stays within [-180, 180] range
    if (targetAngle > 180) targetAngle = 180;
    if (targetAngle < -180) targetAngle = -180;

    digitalWrite(dirPin, direction);
    for (int i = 0; i < stepsToMove; i++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(1500);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(1500);
    }

    currentAngle = targetAngle; // Update current position
    Serial.print("Moved to angle: ");
    Serial.println(currentAngle);
}
