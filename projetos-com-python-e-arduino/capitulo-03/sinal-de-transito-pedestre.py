from pyfirmata import Arduino, OUTPUT

# board = Arduino('/dev/ttyUSB0')

# vermelho_carro = 13
# amarelo_carro = 12
# verde_carro = 11
# verde_pedestre = 10
# vermelho_pedestre = 9

# board.digital[vermelho_carro].mode = OUTPUT
# board.digital[amarelo_carro].mode = OUTPUT
# board.digital[verde_carro].mode = OUTPUT
# board.digital[verde_pedestre].mode = OUTPUT
# board.digital[vermelho_pedestre].mode = OUTPUT

# while True:
#     board.digital[vermelho_carro].write(1)
#     board.digital[verde_pedestre].write(1)
#     board.pass_time(5.0)
#     board.digital[verde_carro].write(1)
#     board.digital[vermelho_pedestre].write(1)
#     board.digital[vermelho_carro].write(0)
#     board.digital[verde_pedestre].write(0)
#     board.pass_time(3.0)
#     board.digital[verde_carro].write(0)
#     board.digital[amarelo_carro].write(1)
#     board.pass_time(1.0)
#     board.digital[amarelo_carro].write(0)


board = Arduino('/dev/ttyUSB0')

vermelho_carro = board.get_pin('d:13:o')
amarelo_carro = board.get_pin('d:12:o')
verde_carro = board.get_pin('d:11:o')
verde_pedestre = board.get_pin('d:10:o')
vermelho_pedestre = board.get_pin('d:9:o')


while True:
    vermelho_carro.write(1)
    verde_pedestre.write(1)
    board.pass_time(5.0)
    verde_carro.write(1)
    vermelho_pedestre.write(1)
    vermelho_carro.write(0)
    verde_pedestre.write(0)
    board.pass_time(3.0)
    verde_carro.write(0)
    amarelo_carro.write(1)
    board.pass_time(1.0)
    amarelo_carro.write(0)