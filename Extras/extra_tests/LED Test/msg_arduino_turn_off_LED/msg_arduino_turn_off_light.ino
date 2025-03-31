void setup() {
  pinMode(13, OUTPUT);  // Set the built-in LED on pin 13 as an output
  Serial.begin(9600);   // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');  // Read the incoming message

    if (message == "ON") {
      digitalWrite(13, HIGH);  // Turn the LED on
      Serial.println("LED turned ON");  // Optional: Send confirmation back to laptop
    } 
    else if (message == "OFF") {
      digitalWrite(13, LOW);  // Turn the LED off
      Serial.println("LED turned OFF");  // Optional: Send confirmation back to laptop
    }
  }
}
