from serial import Serial
import pandas as pd

PATH_D = 'Dados/dados.txt'

ser = Serial()
ser.port = 'COM4'
ser.open()

while True:
    while (ser.inWaiting()==0):
        pass
    arduinoString = ser.readline().decode("utf-8")
    file = open(PATH_D, "at")
    file.write(arduinoString)
    file.close()