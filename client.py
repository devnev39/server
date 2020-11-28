import socket
import cprocess as cp
from os import path as pa

class exit(Exception):
	pass

s = socket.socket()
connected = 1

while(connected):
	try:
		s.connect((socket.gethostname(),8888))
		print('Connected......')
		connected = 0
	except socket.error:
		print('No listener....')

while(True):
	try:
		smg = (s.recv(1024)).decode()

		if(cp.check(smg)):
			print('from server : {0}'.format((smg.split('$'))[1]))
			path = input()
			if(pa.exists(path)):
				fnsz,data = cp.getLsts(path)
				s.send(bytes(fnsz,'ascii'))
				s.send(data)
				print('sent successfully...')
				s.send(bytes(input('you : '),'ascii'))
				continue
			else:
				print('Wrong path...')
				continue				
		print('from server : {0}'.format(smg))
		s.send(bytes(input('you : '),'ascii'))
	except Exception as e:
		print(e)
		print('Exiting... You need to reconnect....')
		break

print('Exiting....')	
input()
