import serial
import time
import csv
import numpy as np
import pandas as pd

timeHr = []
timeT = []
mem1xD = []
mem1yD = []
mem1zD = []
#
mem2xD = []
mem2yD = []
mem2zD = []


arduinoData = serial.Serial('/dev/ttyUSB0')

tStart = str(time.time()).split('.')[0]
fileOut = tStart+'.csv'

while True:
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline().decode("utf-8")

    dataArray = arduinoString.split(",")

    timehr = dataArray[0]
    time = float(dataArray[1])/1000

    mem1x = float(dataArray[2])
    mem1y = float(dataArray[3])
    mem1z = float(dataArray[4])
    #
    mem2x = float(dataArray[5])
    mem2y = float(dataArray[6])
    mem2z = float(dataArray[7])

    timeHr.append(timehr)
    timeT.append(time)
    mem1xD.append(mem1x)
    mem1yD.append(mem1y)
    mem1zD.append(mem1z)
    #
    mem2xD.append(mem2x)
    mem2yD.append(mem2y)
    mem2zD.append(mem2z)

    df = pd.DataFrame({
                        'timeHr':timeHr,
                        'timeT':timeT,
                        'mem1xD':mem1xD,
                        'mem1yD':mem1yD,
                        'mem1zD':mem1zD,
                        'mem2xD':mem2xD,
                        'mem2yD':mem2yD,
                        'mem2zD':mem2zD,

                         }
         )
    df.to_csv(fileOut, mode='a', header=False)