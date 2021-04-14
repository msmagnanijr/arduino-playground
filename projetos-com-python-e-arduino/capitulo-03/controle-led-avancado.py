from pyfirmata import Arduino, OUTPUT

board = Arduino('/dev/ttyUSB0')
board.digital[13].mode = OUTPUT
estado = True
tempo = 0

try:
    while tempo <= 0:
        try:
            tempo = float(input('Digite o tempo: '))
            if tempo <= 0:
                print('ERRO! Digite um número real positivo.')
        except:
            print('ERRO! Digite um número real positivo')
    while True:
        board.digital[13].write(int(estado))
        board.pass_time(tempo)
        estado = not estado
except KeyboardInterrupt:
    board.exit()