import time 
import os 
import serial

ser = serial.Serial {
        port'COMB',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
}

ser.open()
def main(): 
    output = ser.readline()
    data = str(output).split(',')

    del data[0]
    if data: 
        del data[6]
        amp = [float(values) for values in data]
        return amp
    else 
        amp = [0,0,0,0,0,0]
        return amp

if __name__ == "__main__":
    main()
