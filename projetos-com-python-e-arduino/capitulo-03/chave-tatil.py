from pyfirmata import Arduino, INPUT, OUTPUT, util

board = Arduino('/dev/ttyUSB0')
led = 13
botao = 2

it = util.Iterator(board)
it.start()
board.digital[botao].mode = INPUT
board.digital[led].mode = OUTPUT

while True:
    estado = board.digital[botao].read()
    board.digital[led].write(estado)