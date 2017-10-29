import serial

port =  serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.2)

while True:
	rcv = port.readline()
	if len(rcv) > 10:
		print "tag detected: "  + rcv
