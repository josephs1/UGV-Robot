float setpoint = 100;  // Desired speed (RPM)
float measured_value = 0;  // Current speed
float error, last_error;
float integral, derivative;
float Kp = 2.0, Ki = 0.5, Kd = 1.0;  // Tune these values
float output;
unsigned long last_time;

void setup() {
  Serial.begin(9600);
  last_time = millis();
}

void loop() {
  // Read sensor value (simulate with random for example)
  measured_value = analogRead(A0) * 0.1;  // Example conversion

  // Compute error
  error = setpoint - measured_value;

  // Compute integral term
  integral += error * (millis() - last_time);

  // Compute derivative term
  derivative = (error - last_error) / (millis() - last_time);

  // Compute PID output
  output = (Kp * error) + (Ki * integral) + (Kd * derivative);

  // Apply output to motor (simulate by printing)
  Serial.println(output);

  // Update variables
  last_error = error;
  last_time = millis();

  delay(100);  // Small delay for stability
}
