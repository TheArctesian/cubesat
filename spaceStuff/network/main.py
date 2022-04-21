from flask import Flask
from flask_restful import Resource, Api
import time
import numpy
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
def getAmp(): 
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



app = Flask(__name__)
api = Api(app)

class Amp(Resource):
    def get(self):
        amp = getAmp()
        time = os.time
        location = np.array([[x],[y],[z]], np.f32)
        return {
                "Amplitude" : amp,
                "Time" : time, 
                "Location" : location
        }

api.add_resource(Data, 'get/amp')


class Image(Recsource): 
    def get(self) 
        img = filePath
        time = os.time
        location = np.array([[x],[y],[z]], np.f32)
        return {
                "Image" : img,
                "Time" : time, 
                "Location" : location
        }

if __name__ == '__main__':
    app.run(debug=True)

