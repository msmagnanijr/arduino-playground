from pyfirmata import Arduino, OUTPUT

# board = Arduino('/dev/ttyUSB0')
# print('Start')
# while True:
#     board.digital[13].write(1)
#     board.pass_time(0.5)
#     board.digital[13].write(0)
#     board.pass_time(0.5)
# print ('End')

board = Arduino('/dev/ttyUSB0')
led = board.get_pin('d:13:o')

print('Start')

while True:
    board.digital[13].write(1)
    board.pass_time(3)
    board.digital[13].write(0)
    board.pass_time(3)

print ('End')