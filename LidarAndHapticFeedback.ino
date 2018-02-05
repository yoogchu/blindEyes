#include "Adafruit_VL53L0X.h"
#include <Wire.h>
#include "Adafruit_DRV2605.h"

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

Adafruit_DRV2605 drv;
int first = 66;
int second = 53;
int third = 52;
int fourth = 17; // Do quickly
int strong = 14;


void setup() {
  Serial.begin(9600);

  // wait until serial port opens for native USB devices
  while (! Serial) {
    delay(1);
  }
  
  Serial.println("Adafruit VL53L0X test");
  if (!lox.begin()) {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }

  drv.begin();
  
  drv.selectLibrary(1);
  
  // I2C trigger by sending 'go' command 
  // default, internal trigger when sending GO command
  drv.setMode(DRV2605_MODE_INTTRIG); 
  
  // power 
  Serial.println(F("VL53L0X API Simple Ranging example\n\n")); 
}


void loop() {
  VL53L0X_RangingMeasurementData_t measure;
    
  Serial.print("Reading a measurement... ");
  lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!

  if (measure.RangeStatus != 4) {  // phase failures have incorrect data
    int output = measure.RangeMilliMeter;
    Serial.println(output);
    
    if (output > 500) {
      Serial.println("No Buzz");
    }  else if (output > 400) {
      Serial.println(" > 400 < 5qA00");
      drv.setWaveform(0, third);  // play effect 
      drv.setWaveform(1, 0);       // end waveform
      drv.go();
    } else if (output > 300) {
      Serial.println(" > 300 < 400");
      drv.setWaveform(0, fourth);  // play effect 
      drv.setWaveform(1, 0);       // end waveform
      drv.go();
      delay(20);
      drv.setWaveform(0, fourth);  // play effect 
      drv.setWaveform(1, 0);       // end waveform
      drv.go();
    } else if (output > 0) {
      Serial.println(" > 0 < 300");
      drv.setWaveform(0, strong);  // play effect 
      drv.setWaveform(1, 0);       // end waveform
      drv.go();
 
    } 

    
  } else {
    Serial.println(" out of range ");
  }
    
  delay(100);
}
