import serial
import time

uart_port = serial.Serial("/dev/ttyTHS1", baudrate=9600, timeout=3.0)
try:
    while True:
        uart_port.write(b'Hello World!')
        time.sleep(1)
except KeyboardInterrupt:
    uart_port.close()