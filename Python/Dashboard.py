from codecs import utf_8_decode, utf_8_encode
from encodings import utf_8
from serial import Serial, SerialException
from time import sleep


def dados(cont, data):
    print('OK')
    ent =  'Dados/dados_'+ str(cont) + '.txt'
    file = open(ent, "at")
    file.write(data)
    file.close()

i = 0

while True:
    try:
        ser = Serial('COM4')
        sleep(2) # Entre 1.5s a 2s
        if not ser.isOpen():
            print('Close')
        else:           
            arduinoS = ser.readline().decode("utf-8")
            dados(i, arduinoS)
            ser.close()
        
    except SerialException:
        i = i + 1
        print ('Error')
        sleep(1)