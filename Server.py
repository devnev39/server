import Process as processor
import socket
import concurrent.futures

lst_con = []

cmd = 'get_cons : get all client\nconnect $<addr> : conenct to a client\nexiT0 : exit'

def start(port):
	s = socket.socket()
	try:
		s.bind((socket.gethostname(),1234))
		s.listen(0)
		print('In listening state.....')

	except Exception as e:
		print('Server Exception : {0}'.format(e))
		s = 0
	
	try:		
	
		with concurrent.futures.ThreadPoolExecutor() as executor:
			while(True):
				acc,addr = s.accept()
				print('Connection from : {0}'.format(addr))
				acc.send(bytes(f'You : {addr} \n {cmd}','ascii')) #main2
				lst_con.append(str(addr))
				processor.process(acc,addr,lst_con)

	except Exception as e:
		print('Threading Exception : {0}'.format(e))				

