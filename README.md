# AWS IoT Workshop

Hands on workshop for Chariot Solutions' [IoT on AWS Conference](https://chariotsolutions.com/event/iot-on-aws-smart-devices-are-just-the-beginning/).

The workshop will use the Arduino MKR WiFi 1010 board with the MRK ENV shield.

Arduino MKR WiFi 1010 

 * https://store.arduino.cc/usa/mkr-wifi-1010 
 * https://www.arduino.cc/en/Guide/MKRWiFi1010

Arduino MKR ENV Shield

 * https://store.arduino.cc/usa/mkr-env-shield
 * https://www.arduino.cc/en/Guide/MKRENVShield
 
The ENV shield has a bunch of sensors

 * Atmospheric Pressure, ST LPS22HB
 * Temperature and Humidity, ST HTS221
 * Ambient Light LUX, Vishay TEMT6000X01
 * Ultraviolet Index (UVA UVB), VEML6075

MKR ENV library allows us to access the sensors through a common library https://www.arduino.cc/en/Reference/ArduinoMKRENV

The workshop materials will walk through connecting the Arduino MKR 1010 to [AWS IoT Core](https://aws.amazon.com/iot-core/).

## Kinesis Analytics

See [KinesisAnalyticsExample/README.md](KinesisAnalyticsExample/README.md) for instructions on how to run the Kinesis Analytics exercise.

## Device Shadows

Sample iOS and Arduino code for using device shadows can be found in the [aws-mobile-iot](https://github.com/chariotsolutions/aws-mobile-iot)repo.
