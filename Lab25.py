import serial
import time
# --- Configure your COM port and baud rate ---
# Example: COM3 for Windows, /dev/ttyUSB0 for Linux
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)   # Wait for Arduino to reset
print("Connection established. Sending messages...\n")
while True:
    message = input("Enter message to send (or 'exit' to quit): ")
 if message.lower() == 'exit':
        print("Closing connection...")
        arduino.close()
        break

message += "\n"               # Add newline so Arduino knows message ended
arduino.write(message.encode())  # Send message as bytes
print(f"Sent: {message}")

#Arduino Code:
    void setup() {
  Serial.begin(9600);
  Serial.println("Arduino Ready");
}
void loop() {
  if (Serial.available()) {
    String msg = Serial.readStringUntil('\n');
    Serial.print("Received: ");
    Serial.println(msg);
  }
}
