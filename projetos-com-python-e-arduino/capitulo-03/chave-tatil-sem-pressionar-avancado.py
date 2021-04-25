from pyfirmata import Arduino, INPUT, OUTPUT, util

board = Arduino('/dev/ttyUSB0')

led1 = 11
led2 = 12
led3 = 13
botao = 2
anterior = False
num = 0

digito = [
    [0, 0, 0 ],
    [0, 0, 1 ],
    [0, 1, 0 ],
    [0, 1, 1 ],
    [1, 0, 0 ],
    [1, 0, 1 ],
    [1, 1, 0 ],
    [1, 1, 1 ]
]

it = util.Iterator(board)
it.start()

board.digital[botao].mode = INPUT
board.digital[led1].mode = OUTPUT
board.digital[led2].mode = OUTPUT
board.digital[led3].mode = OUTPUT

while True:
    valor = board.digital[botao].read()
    if valor == True and anterior == False:
        num = num + 1
        if num > 7:
            num = 0
        print('Decimal:', num, 'Binário:',
            str('{0:b}'.format(num)).zfill(3))
        board.digital[led1].write(digito[num][0])
        board.digital[led2].write(digito[num][1])
        board.digital[led3].write(digito[num][2])
    anterior = valor
    board.pass_time(0.05)