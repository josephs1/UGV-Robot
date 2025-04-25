// Pin assignments
const int dirPin = 3;    // Direction pin (DIR+)
const int stepPin = 2;   // Step pin (PUL+)
const int microstepping = 8; // Might need to change to 32.
const int stepsPerRevolution = 200 * microstepping; // Full steps (1.8° per step)
const float degreesPerStep = 360.0 / stepsPerRevolution; // = 1.8 if no microstepping
float currentAngle = 0.0;     // Track current position

void setup() {
    pinMode(stepPin, OUTPUT);
    pinMode(dirPin, OUTPUT);
    Serial.begin(9600);
    Serial.println("Stepper ready. Enter target angle:");
  }
  
void loop() {
  // Negative Direction is Clockwise Rotation on the rightside of the arm, making the arm move down.
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim(); // Remove whitespace
    float targetAngle = input.toFloat();

    float angleDiff = targetAngle - currentAngle;
    int direction = (angleDiff >= 0) ? HIGH : LOW;
    int stepsToMove = abs(angleDiff) / degreesPerStep;

    digitalWrite(dirPin, direction);
    for (int i = 0; i < stepsToMove; i++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(1500);  // fastest speed is 75
      digitalWrite(stepPin, LOW);
      delayMicroseconds(1500);
    }

    currentAngle = targetAngle;
    Serial.print("Moved to angle: ");
    Serial.println(currentAngle);
  }
}
