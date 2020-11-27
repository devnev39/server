import Process as processor
import socket
import threading

lst_con = []

cmd = 'get_cons : get all client\nconnect $<addr> : conenct to a client\nexiT0 : exit'

def start(port):
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		s.bind((socket.gethostname(),port))
		s.listen(0)
		print('In listening state.....')

	except Exception as e:
		print('Server Exception : {0}'.format(e))
		s = 0
		return
	
	try:		

		while(True):
			acc,addr = s.accept()
			print('Connection from : {0}'.format(addr))
			acc.send(bytes(f'You : {addr} \n {cmd}','ascii')) #main2
			lst_con.append(str(addr))
			
			t = threading.Thread(target=processor.process,args=(acc,addr,lst_con))
			t.daemon = True
			t.start()

	except Exception as e:
		print('Threading Exception : {0}'.format(e))	
		return			

