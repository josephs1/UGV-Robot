// Right side Motors need to be negative speed.
#include <Servo.h>

// Motor Pins
#define FRONT_LEFT_MOTOR 8  
#define BACK_LEFT_MOTOR 9 
#define FRONT_RIGHT_MOTOR 7  
#define BACK_RIGHT_MOTOR 6

// Spark MAX Motor Controllers
Servo frontLeftController; 
Servo backLeftController; 
Servo frontRightController; 
Servo backRightController; 

String inputString = "";
float left_wheel_speed = 0.0;
float right_wheel_speed = 0.0;

void setup() {
    Serial.begin(9600); // Start serial communication
    frontLeftController.attach(FRONT_LEFT_MOTOR);
    backLeftController.attach(BACK_LEFT_MOTOR);    
    frontRightController.attach(FRONT_RIGHT_MOTOR);
    backRightController.attach(BACK_RIGHT_MOTOR); 
    Serial.println("Enter speed (-1.0 to 1.0):");
}

void loop() {
//    if (Serial.available() > 0) {
//        String input = Serial.readStringUntil('\n'); // Read input until newline
//        input.trim(); // Remove leading/trailing whitespace
//
//        float speed = input.toFloat(); // Convert to float
//        speed = constrain(speed, -1.0, 1.0); // Constrain to range
//        
//        int pulseWidth = mapSpeedToPWM(speed); // Convert to PWM
//        
//        frontLeftController.writeMicroseconds(mapSpeedToPWM(0)); // Stop motors
//        backLeftController.writeMicroseconds(mapSpeedToPWM(0));
//        delay(300);
//        frontLeftController.writeMicroseconds(pulseWidth); // Send to motors
//        backLeftController.writeMicroseconds(pulseWidth);
//
//        Serial.print("Set speed to: ");
//        Serial.println(speed);
//    }
      delay(2000);
      float speed = 0.25; // Convert to float
      speed = constrain(speed, -1.0, 1.0); // Constrain to range
      int pulseWidth = mapSpeedToPWM(speed);
      int pulseWidth2 = mapSpeedToPWM(-1.0*speed);
      int pulseWidth0 = mapSpeedToPWM(0);
      frontLeftController.writeMicroseconds(pulseWidth); // Stop motors
      backLeftController.writeMicroseconds(pulseWidth);
      frontRightController.writeMicroseconds(pulseWidth2); // Stop motors
      backRightController.writeMicroseconds(pulseWidth2);
      delay(2500);
      frontLeftController.writeMicroseconds(pulseWidth0); // Stop motors
      backLeftController.writeMicroseconds(pulseWidth0);
      frontRightController.writeMicroseconds(pulseWidth0); // Stop motors
      backRightController.writeMicroseconds(pulseWidth0);
      delay(2500);
      speed = -0.25;
      pulseWidth = mapSpeedToPWM(speed);
      pulseWidth2 = mapSpeedToPWM(-1.0*speed);
      frontLeftController.writeMicroseconds(pulseWidth); // Stop motors
      backLeftController.writeMicroseconds(pulseWidth);
      frontRightController.writeMicroseconds(pulseWidth2); // Stop motors
      backRightController.writeMicroseconds(pulseWidth2);
      delay(2500);
      frontLeftController.writeMicroseconds(pulseWidth0); // Stop motors
      backLeftController.writeMicroseconds(pulseWidth0);
      frontRightController.writeMicroseconds(pulseWidth0); // Stop motors
      backRightController.writeMicroseconds(pulseWidth0);
      delay(20000);
}

// Function to map speed (-1.0 to 1.0) to PWM pulse width (1000 to 2000 μs)
int mapSpeedToPWM(float speed) {
    return map(speed * 100, -100, 100, 1000, 2000);
}
