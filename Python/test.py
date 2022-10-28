import serial.tools.list_ports
    
def find_arduino(port=None):
    """Captura o nome da porta que o Arduino se encontra"""
    if port is None:
        ports = serial.tools.list_ports.comports()
        for p in ports:
            #if p.manufacturer is not None and "Arduino" in p.manufacturer:
               #port = p.manufacturer
            if p.manufacturer is not None:
                port = p.device
    return port

port = find_arduino();


print (port)
