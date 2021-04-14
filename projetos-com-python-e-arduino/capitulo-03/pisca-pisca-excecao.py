from pyfirmata import Arduino, OUTPUT

board = Arduino('/dev/ttyUSB0')

try:
    while True:
        board.digital[13].write(1)
        board.pass_time(0.5)
        board.digital[13].write(0)
        board.pass_time(0.5)
except KeyboardInterrupt:
    board.exit
