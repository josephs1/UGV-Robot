void setup() {
  Serial.begin(9600); // Start Serial communication at 9600 baud rate
  while (!Serial);    // Wait for Serial to initialize (necessary for Due)
  Serial.println("Arduino ready to receive messages...");
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming string
    String receivedMessage = Serial.readStringUntil('\n');
    receivedMessage.trim(); // Remove any trailing whitespace or newline characters

    // Print the received message to the Serial monitor
    Serial.print("Message received: ");
    Serial.println(receivedMessage);

    // Optional: Send a response back to the Jetson
    Serial.println("Message acknowledged.");
  }
}
