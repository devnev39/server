import socket
import cprocess as cp
from os import path as pa
from time import perf_counter as pf
import sys

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
				File = cp.getLsts(path)
				s.send(bytes(File.fnsz,'ascii'))
				
				data = File.file.read(4096)
				st = pf()
				while(data):
					acc.send(data)
					print('packed sent')
					data = File.file.read(4096)
				fn = pf()
				print(f'sent successfully...\n speed : {File.size/round(fn-st,2)}')
				s.send(bytes(input('you : '),'ascii'))
				continue
			else:
				print('Wrong path...')
				continue				
		print('from server : {0}'.format(smg))
		s.send(bytes(input('you : '),'ascii'))
	except Exception as e:
		ext,exobj,exwhere = sys.exc_info()
		print(e)
		print(f'Exiting... You need to reconnect.... {exwhere.tb_lineno}')
		break

print('Exiting....')	
input()
