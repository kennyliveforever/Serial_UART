void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("OK");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    Serial.println(command);
}
}
