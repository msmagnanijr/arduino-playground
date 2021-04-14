from pyfirmata import Arduino, OUTPUT

# board = Arduino('/dev/ttyUSB0')
# board.digital[13].mode = OUTPUT

# while True:
#     estado = input('Digite 1 para ligar o LED ou 0 para desligar: ')
#     board.digital[13].write(int(estado))


board = Arduino('/dev/ttyUSB0')
board.digital[13].mode = OUTPUT

while True:
    estado = input('Digite 1 para ligar o LED ou 0 para desligar: ')
    if estado == '0' or estado == '1':
        board.digital[13].write(int(estado))
    else:
       print('ERRO: Digite apenas 0 ou 1!')