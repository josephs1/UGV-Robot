#include <Servo.h>
// #include <Wire.h>
// #include <Adafruit_PWMServoDriver.h>

// Motor Pins
#define LEFT_MOTOR_1 8  
#define LEFT_MOTOR_2 9 
#define RIGHT_MOTOR_1 7  
#define RIGHT_MOTOR_2 6

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
          float tempLeft = inputString.substring(0, commaIndex).toFloat();
          float tempRight = inputString.substring(commaIndex + 1).toFloat();

          // Only assign if valid
          left_wheel_speed = (tempLeft*-1.0)/2.0;
          right_wheel_speed = (tempRight)/2.0;
          
          // Set Motor Speed
          if (-0.1 < left_wheel_speed < 1.0){
            left_wheel_motor1.writeMicroseconds(speedToPulseWidth(0));
            left_wheel_motor2.writeMicroseconds(speedToPulseWidth(0));
            right_wheel_motor1.writeMicroseconds(speedToPulseWidth(0));
            right_wheel_motor2.writeMicroseconds(speedToPulseWidth(0));
          }
          else{
            left_wheel_motor1.writeMicroseconds(speedToPulseWidth(left_wheel_speed));
            left_wheel_motor2.writeMicroseconds(speedToPulseWidth(left_wheel_speed));
            right_wheel_motor1.writeMicroseconds(speedToPulseWidth(right_wheel_speed));
            right_wheel_motor2.writeMicroseconds(speedToPulseWidth(right_wheel_speed));
          }

          // Print to Serial Monitor
          Serial.println("Received: " + inputString);
          Serial.print("Left: "); Serial.println(left_wheel_speed);
          Serial.print("Right: "); Serial.println(right_wheel_speed);
        }
      }
      inputString = "";
    }
    else {
      inputString += c;
    }
  }  
  delay(50);
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
