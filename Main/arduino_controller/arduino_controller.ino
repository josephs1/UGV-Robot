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

// Spark MAX Motor Controllers
Servo left_wheel_motor1; 
Servo left_wheel_motor2;
Servo right_wheel_motor1; 
Servo right_wheel_motor2; 

String inputString = "";
float left_wheel_speed = 0.0;
float right_wheel_speed = 0.0;

int servoPos1 = 0;
int servoPos2 = 0;
int servoPos3 = 0;

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
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      inputString.trim();
      if (inputString == "exit") {
        // Do nothing
      }
      else {
        int commaIndex = inputString.indexOf(',');
        if (commaIndex > 0) {
          String command = inputString.substring(0, commaIndex);
          String args = inputString.substring(commaIndex + 1);
          Serial.flush();

          if (command == "nema") {
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
          }
          else if (command == "servo1") {
            int dir = args.toFloat();
            int delta = 15;
            servoPos1 += int(dir * delta);
            servoPos1 = constrain(servoPos1, 0, 270);
            moveServo(servo1, servoPos1);
        
            Serial.print("servo1 moved to ");
            Serial.print(servoPos1);
            Serial.println(" degrees");
          }
          else if (command == "servo2") {
            int dir = args.toFloat();
            int delta = 15;
            servoPos2 += int(dir * delta);
            servoPos2 = constrain(servoPos2, 0, 270);
            moveServo(servo2, servoPos2);
        
            Serial.print("servo2 moved to ");
            Serial.print(servoPos2);
            Serial.println(" degrees");
          }
          else if (command == "servo3") {
            int dir = args.toFloat();
            int delta = 15;
            servoPos3 += int(dir * delta);
            servoPos3 = constrain(servoPos3, 0, 270);
            moveServo(servo3, servoPos3);
        
            Serial.print("servo3 moved to ");
            Serial.print(servoPos3);
            Serial.println(" degrees");
          }
          else if (command == "drive"){
            int commaIndex2 = args.indexOf(',');
            if (commaIndex2 > 0){
              float tempLeft = args.substring(0, commaIndex2).toFloat();
              float tempRight = args.substring(commaIndex2 + 1).toFloat();
              
              left_wheel_speed = (tempLeft*-1.0)/3.0;
              right_wheel_speed = (tempRight)/3.0;

              // Set Left Motor Speed
              if (left_wheel_speed > -0.03 && left_wheel_speed < 0.03){
                left_wheel_motor1.writeMicroseconds(speedToPulseWidth(0));
                left_wheel_motor2.writeMicroseconds(speedToPulseWidth(0));
                
              }
              else{
                left_wheel_motor1.writeMicroseconds(speedToPulseWidth(left_wheel_speed));
                left_wheel_motor2.writeMicroseconds(speedToPulseWidth(left_wheel_speed));
              }

              // Set Right Motor Speed
              if (right_wheel_speed > -0.03 && right_wheel_speed < 0.03){
                right_wheel_motor1.writeMicroseconds(speedToPulseWidth(0));
                right_wheel_motor2.writeMicroseconds(speedToPulseWidth(0));
              }
              else {
                right_wheel_motor1.writeMicroseconds(speedToPulseWidth(right_wheel_speed));
                right_wheel_motor2.writeMicroseconds(speedToPulseWidth(right_wheel_speed));
              }

              // Print to Serial Monitor
              Serial.println("Received: " + inputString);
              Serial.print("Left: "); Serial.println(left_wheel_speed);
              Serial.print("Right: "); Serial.println(right_wheel_speed);
            }
          }
        }
      }
      inputString = "";
      lastDataTime = millis();
    }
    else {
      inputString += c;
    }
  }
  // Check for timeout and stop motors if necessary
  if (millis() - lastDataTime > timeoutDuration) {
    stopMotors();
  }  
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
