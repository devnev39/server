import socket

s = socket.socket()
connected = 1

while(connected):
	try:
		s.connect((socket.gethostname(),1234))
		print('Connected......')
		connected = 0
	except socket.error:
		print('No listener....')

while(True):
	print('from server : {0}'.format((s.recv(1024)).decode()))
	s.send(bytes(input('you : '),'ascii'))

	

