void setup() {
  Serial.begin(9600);  // Initialize serial communication with the Jetson
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');  // Read the incoming message
    command.trim();  // Remove any trailing newline or spaces

    // Respond to the message
    if (command == "UP") {
      Serial.println("Arduino received: UP");
    }
    else if (command == "DOWN") {
      Serial.println("Arduino received: DOWN");
    }
    else if (command == "LEFT") {
      Serial.println("Arduino received: LEFT");
    }
    else if (command == "RIGHT") {
      Serial.println("Arduino received: RIGHT");
    }
    else {
      Serial.println("Unknown command");
    }
  }
}
