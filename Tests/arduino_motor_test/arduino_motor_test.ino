//This code is for controlling servos connected to a PCA9685 Servo Driver Board
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define MIN_PULSE_WIDTH 500
#define MAX_PULSE_WIDTH 2500
#define FREQUENCY 50

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define servo1 0
#define delay_time 2000

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);   // Initialize serial communication.
  pwm.begin();
  pwm.setPWMFreq(FREQUENCY);
  //myServo.attach(9); // Attach servo signal to pin 9.
}

void moveServo(int servoOut, int angle){
  int pulseWidth = map(angle, 0, 270, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
  // Convert the pulse width to a value suitable for the PCA9685
  int pulseValue = int(float(pulseWidth) / 1000000 * FREQUENCY * 4096);
  pwm.setPWM(servoOut, 0, pulseValue);
}

void loop() {
  //Initial Delay
  delay(1000);

  moveServo(servo1, 0);
//  moveServo(servo2, 0);
//  moveServo(servo80kg, 0);
  delay(delay_time);

  moveServo(servo1, 90);
//  moveServo(servo2, 0);
//  moveServo(servo80kg, 0);
  delay(delay_time);

  moveServo(servo1, 180);
//  moveServo(servo2, 0);
//  moveServo(servo80kg, 0);
  delay(delay_time);

  moveServo(servo1, 270);
//  moveServo(servo2, 90);
//  moveServo(servo80kg, 90);
  delay(delay_time);
  

//  moveServo(servo1, 270);
//  moveServo(servo2, 270);
//  moveServo(servo80kg, 270);

  // Move motor to 90 degrees
  

  // Move motor to 180 degrees
//  moveServo(servo1,110);
//  delay(3000);

  // Move motor to 270 degrees
//  moveServo(servo1, 270);
//  delay(2500);
  
   //Move from 0° to 180°
//  for (int pos = 0; pos <= 180; pos += 10){
//    myServo.write(pos);
//    delay(1000); //Adjust delay for smooth movement
//  }
//
//  delay(3000); // Wait at 0°
//  for (int pos = 180; pos >= 0; pos -= 10){
//    myServo.write(pos);
//    delay(1000); //Adjust delay for smooth movement
//  }

//  myServo.write(0);
//  delay(2000);
//  myServo.write(180);
//  delay(2000);
}
