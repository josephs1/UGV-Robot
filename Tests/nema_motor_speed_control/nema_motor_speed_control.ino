const int dirPin = 3;    // Direction pin (DIR+)
const int stepPin = 2;   // Step pin (PUL+)
const int microstepping = 8;
const int stepsPerRevolution = 200 * microstepping; // 1.8° per step * microstepping
const float degreesPerStep = 360.0 / stepsPerRevolution;

// Speed control
int speed = 500; // Steps per second — change this to test speed
unsigned long stepDelay = 1000000 / speed; // microseconds between steps

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Stepper running for 5 seconds...");

  digitalWrite(dirPin, HIGH); // Set direction

  unsigned long startTime = millis();
  while (millis() - startTime < 5000) { // Run for 5 seconds
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(stepDelay / 2);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(stepDelay / 2);
  }

  Serial.println("Stepper stopped.");
}

void loop() {
  // Nothing to do in loop for now
}
