import time
from ADCDevice import *

adc = ADCDevice() # Define an ADCDevice class object

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)

def loop():
    while True:
        value0 = adc.analogRead(0)    # read the ADC value of channel 0
        value1 = adc.analogRead(1)    # read the ADC value of channel 1
        voltage0 = value0 / 255.0 * 3.3
        voltage1 = value1 / 255.0 * 3.3
        print ('ADC Value 1 : %d, Voltage 1 : %.2f, ADC Value 2 : %d, Voltage 2 : %.2f'%(value0,voltage0,value1,voltage1))
        time.sleep(0.01)

def destroy():
    adc.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")
        
