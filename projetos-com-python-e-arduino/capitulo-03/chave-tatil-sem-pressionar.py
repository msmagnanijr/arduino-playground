from pyfirmata import Arduino, INPUT, OUTPUT, util

board = Arduino('/dev/ttyUSB0')
led = 13
botao = 2
anterior = False
estado = False

it = util.Iterator(board)
it.start()

board.digital[botao].mode = INPUT
board.digital[led].mode = OUTPUT

while True:
    valor = board.digital[botao].read()
    if valor == True and anterior == False:
        estado = not estado
        print('LED', estado)
        board.digital[led].write(estado)
    anterior = valor
    board.pass_time(0.05)