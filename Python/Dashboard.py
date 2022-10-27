from serial import Serial, SerialException
import serial.tools.list_ports
from time import sleep


i = 0

def dados(cont, data):
    ent =  'Dados/dados_'+ str(cont) + '.txt'
    file = open(ent, "at")
    file.write(data)
    file.close()

def find_arduino(port=None):
    """Captura o nome da porta que o Arduino se encontra"""
    if port is None:
        ports = serial.tools.list_ports.comports()
        for p in ports:
            if p.manufacturer is not None and "Arduino" in p.manufacturer:
                port = p.device
    return port


while True:
    try:
        port = find_arduino()
        ser = Serial(port)
        sleep(2) # Entre 1.5s a 2s
        while port!=None:
            print('ok') 
            arduinoS = ser.readline().decode("utf-8")
            dados(i, arduinoS)
            port = find_arduino()
        ser.close() 
        
    except SerialException:
        i = i + 1 
        print ('Error')
        sleep(2)