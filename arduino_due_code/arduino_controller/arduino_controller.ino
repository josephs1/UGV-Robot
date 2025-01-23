void setup() {
  Serial.begin(9600);   // Initialize serial communication
  pinMode(13, OUTPUT);  // Set the built-in LED on pin 13 as an output
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');  // Read the command until newline
    command.trim();  // Remove any trailing newline or spaces

    if (command == "UP" || command == "DOWN" || command == "LEFT" || command == "RIGHT") {
      Serial.println("Command received: " + command);
      digitalWrite(13, HIGH);  // Turn on the LED
      delay(1000);  // Wait for 1 second
      digitalWrite(13, LOW);  // Turn off the LED
      Serial.println("LED turned off");
    } 
    else {
      Serial.println("Unknown Command");
    }
  }
}
