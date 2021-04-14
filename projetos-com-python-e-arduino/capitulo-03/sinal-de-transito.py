from pyfirmata import Arduino, OUTPUT

# board = Arduino('/dev/ttyUSB0')
# vermelho = 13
# amarelo = 12
# verde = 11

# board.digital[vermelho].mode = OUTPUT
# board.digital[amarelo].mode = OUTPUT
# board.digital[verde].mode = OUTPUT

# while True:
#     board.digital[vermelho].write(1)
#     board.pass_time(5.0)
#     board.digital[vermelho].write(0)
#     board.digital[verde].write(1)
#     board.pass_time(3.0)
#     board.digital[verde].write(0)
#     board.digital[amarelo].write(1)
#     board.pass_time(1.0)
#     board.digital[amarelo].write(0)


board = Arduino('/dev/ttyUSB0')
vermelho  = board.get_pin('d:13:o')
amarelo = board.get_pin('d:12:o')
verde = board.get_pin('d:11:o')

while True:
    vermelho.write(1)
    board.pass_time(5.0)
    vermelho.write(0)
    verde.write(1)
    board.pass_time(10.0)
    verde.write(0)
    amarelo.write(1)
    board.pass_time(1.0)
    amarelo.write(0)