import serial

"""
    Asergurarse de que es el puerto correcto 
    y la velocidad de transmisión es la correcta
    en la siguiente línea.

    Comando para ver puertos en Linux:
    ls /dev/tty*
"""
ser = serial.Serial('/dev/ttyUSB0', 9600) #

try:
    while True:
        # Lee datos del puerto serie
        data = ser.readline().decode().strip()
        print("Dato recibido:", data)

except KeyboardInterrupt:
    ser.close() # Cierra el puerto serie cuando se interrumpe el programa
