import serial

gps = serial.Serial("/dev/ttyACM0", baudrate = 9600)

while True:
	line = gps.readline()
	data = line.split(",")
	if data[0] == "$GPRMC":
		print line
