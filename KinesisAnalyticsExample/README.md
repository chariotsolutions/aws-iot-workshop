# DON'T USE THIS REPO!!!!!

NEW REPO: https://github.com/chariotsolutions/aws-iot-workshop

# chariot-fall-2019-workshop
Temp repository for the Chariot Fall 2019 IoT Workshop. Content here will eventually get moved into the official repo.

For details on setting up AWS Core IoT, creating certs, etc see https://github.com/don/ITP-DeviceToDatabase/blob/master/07_AWS/aws.md

The proposed hardware is the Arduino MKR WiFi 1010 board with the MRK ENV shield

Arduino MKR WiFi 1010 

 * https://store.arduino.cc/usa/mkr-wifi-1010 
 * https://www.arduino.cc/en/Guide/MKRWiFi1010

Arduino MKR ENV Shield

 * https://store.arduino.cc/usa/mkr-env-shield
 * https://www.arduino.cc/en/Guide/MKRENVShield

The ENV shield has a bunch of sensors

 * Atmospheric Pressure, ST LPS22HB, https://www.st.com/resource/en/datasheet/dm00140895.pdf
 * Temperature and Humidity, ST HTS221, https://www.st.com/resource/en/datasheet/hts221.pdf
 * Ambient Light LUX, Vishay TEMT6000X01, https://www.vishay.com/docs/81579/temt6000.pdf
 * Ultraviolet Index (UVA UVB), VEML6075, https://www.vishay.com/docs/84304/veml6075.pdf datasheet link is broken maybe see https://www.vishay.com/docs/84277/veml6070.pdf for an idea of how it works

MKR ENV library allows us to access the sensors through a common library https://www.arduino.cc/en/Reference/ArduinoMKRENV

Use the Arduino IDE's Library Manager to install the MKRENV library

![Arduino Library Manager screenshot with MKRENV library](library-mkrenv.png)

Sample iOS and Arduino code for using device shadows can be found here: https://github.com/chariotsolutions/aws-mobile-iot
