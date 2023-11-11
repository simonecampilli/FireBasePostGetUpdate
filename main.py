import serial

arduino = serial.Serial('COM3', 9600)  # Sostituisci 'COMX' con la porta seriale appropriata

while True:
    comando = input("Inserisci 1 per accendere il LED o 0 per spegnerlo: ")
    arduino.write(comando.encode())
