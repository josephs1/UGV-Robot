#include <Servo.h>

Servo myServo; // Create a Servo object

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);   // Initialize serial communication.
  myServo.attach(9); // Attach servo signal to pin 9.
}

void loop() {
  // Move from 0° to 180°
  for (int pos = 0; pos <= 180; pos += 5){
    myServo.write(pos);
    delay(20); //Adjust delay for smooth movement
  }

  delay(1000); // Wait at 0°
}
