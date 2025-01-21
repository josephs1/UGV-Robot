void setup() {
  Serial.begin(9600); // Initialize Serial communication
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read the command
    command.trim(); // Remove any trailing newline or spaces

    if (command == "UP") {
      Serial.println("Arrow Key Pressed: UP");
    }
    else if (command == "DOWN") {
      Serial.println("Arrow Key Pressed: DOWN");
    }
    else if (command == "LEFT") {
      Serial.println("Arrow Key Pressed: LEFT");
    }
    else if (command == "RIGHT") {
      Serial.println("Arrow Key Pressed: RIGHT");
    }
    else {
      Serial.println("Unknown Command");
    }
  }
}

