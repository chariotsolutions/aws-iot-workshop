/*
  MKR ENV Shield - Read Sensors

  This example reads the sensors on-board the MKR ENV shield
  and prints them to the Serial Monitor once a second.

  The circuit:
  - Arduino MKR board
  - Arduino MKR ENV Shield attached
  - LED on Pin 5

  This example code is in the public domain.

  This example is based on https://github.com/arduino-libraries/Arduino_MKRENV/blob/master/examples/ReadSensors/ReadSensors.ino
*/

#include <Arduino_MKRENV.h>
const int ledPin = 5;

void setup() {

  // initialize the LED as an output
  pinMode(ledPin, OUTPUT);
  // turn the LED on
  digitalWrite(ledPin, HIGH);
  
  Serial.begin(9600);
  while (!Serial);

  if (!ENV.begin()) {
    Serial.println("Failed to initialize MKR ENV shield!");
    while (1);
  }
}

void loop() {
  // turn the LED on
  digitalWrite(ledPin, HIGH);
  
  // read all the sensor values
  float temperature = ENV.readTemperature(FAHRENHEIT);
  float humidity    = ENV.readHumidity();
  float pressure    = ENV.readPressure();
  float illuminance = ENV.readIlluminance();
  float uva         = ENV.readUVA();
  float uvb         = ENV.readUVB();
  float uvIndex     = ENV.readUVIndex();

  // print each of the sensor values
  Serial.print("Temperature = ");
  Serial.print(temperature);
  Serial.println(" °F");

  Serial.print("Humidity    = ");
  Serial.print(humidity);
  Serial.println(" %");

  Serial.print("Pressure    = ");
  Serial.print(pressure);
  Serial.println(" kPa");

  Serial.print("Illuminance = ");
  Serial.print(illuminance);
  Serial.println(" lx");

  Serial.print("UVA         = ");
  Serial.println(uva);

  Serial.print("UVB         = ");
  Serial.println(uvb);

  Serial.print("UV Index    = ");
  Serial.println(uvIndex);

  // print an empty line
  Serial.println();

  // wait 
  delay(750);

  // Turn the LED off
  digitalWrite(ledPin, LOW);

  // wait 1 second to print again
  delay(1000);
}
