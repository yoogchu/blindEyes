/*
    TODO: Add thresholding
*/
#include "mbed.h"
#include "ultrasonic.h" // Sonar
#include "DRV2605.h" // Haptic
#include "VL53L0X.h" // Tof
 
#define range1_addr (0x56)
#define range2_addr (0x60)
#define range1_XSHUT   p26
#define range2_XSHUT   p25
#define VL53L0_I2C_SDA   p28
#define VL53L0_I2C_SCL   p27

Serial pc(USBTX,USBRX);
static DevI2C devI2c(VL53L0_I2C_SDA,VL53L0_I2C_SCL); 

DRV2605 haptics(p9, p10);
bool sonar = false;

 void dist(int distance)
{
    //put code here to execute when the distance has changed
    printf("\n\nDistance Sonar      %d mm\r\n", distance);
    if (distance < 900 && distance > 10)
        sonar = true;
}

ultrasonic mu(p6, p7, .1, 1, &dist);    //Set the trigger pin to D8 and the echo pin to D9
                                        //have updates every .1 seconds and a timeout after 1
                                        //second, and call dist when the distance changes
int main()
{
    // Sonar Object
    mu.startUpdates();//start measuring the distance
    
    // ToF sensors
    /*Contruct the sensors*/ 
    static DigitalOut shutdown1_pin(range1_XSHUT);
    static VL53L0X range1(&devI2c, &shutdown1_pin, NC);
    static DigitalOut shutdown2_pin(range2_XSHUT);
    static VL53L0X range2(&devI2c, &shutdown2_pin, NC);
    /*Initial all sensors*/   
    range1.init_sensor(range1_addr);
    range2.init_sensor(range2_addr);
    
    /*Get datas*/
    uint32_t distance1;
    uint32_t distance2;
    int status1;
    int status2;
    
    // Haptic Driver
    /* Daignostics Routine */
    printf("Diagnostics Result: %X\n", haptics.diagnostics());        
    // Initialization Procedure as outlined in Section 9.3 of Device Datasheet
    printf("Calibration Result: %X\n",haptics.init(3.3));    
    // Daignostics Routine
    printf("Diagnostics Result: %X\n", haptics.diagnostics());
    
    /*
    // Play sequence of library waveforms as outlined in Section 9.3.2.1 of Device Datasheet
    haptics.load_waveform_sequence(123,21,43,18,94,48,112,36);
    haptics.play();
    while(haptics.i2cReadByte(GO));         // Wait for playback to complete     
    */
    
    while(1)
    {
        /* Sonar */
        mu.checkDistance();     //call checkDistance() as much as possible, as this is where
                                //the class checks if dist needs to be called.
         
        /* ToF Sensors */                       
        status1 = range1.get_distance(&distance1);
        
        if (status1 == VL53L0X_ERROR_NONE) {
            printf("T1:   %6ld\r\n", distance1);
        } else {
            printf("T1:   --\r\n");
        }
 
        status2 = range2.get_distance(&distance2);
        if (status2 == VL53L0X_ERROR_NONE) {
            printf("T2:   %6ld\r\n", distance2);
        } else {
            printf("T2:   --\r\n");
        }
        // Single threshold for demo purposes. Edit later.
        if ((status1 < 400 && status1 > 10) || (status2 < 400 && status2 > 10) || (sonar)) {
            printf("BUZZZZZZZZZZZZZ\n");
            sonar = false;
            haptics.load_waveform_sequence(123,21,112);
            haptics.play();
            while(haptics.i2cReadByte(GO));         // Wait for playback to complete
            wait(0.1);
        }      
    }
}
