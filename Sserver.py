import socket
import threading
import os 
import sys

lst_con = []

class exit(Exception):
	pass

def constr():
	s = ''
	for e in lst_con:
		s+=e+'\n'

	return s		

cmd = 'get_cons : get all client\nconnect $<addr> : conenct to a client\nexiT0 : exit'

s = socket.socket()
try:
	s.bind((socket.gethostname(),1234))
	s.listen(0)
	print('In listening state.....')

	def getCons():
		s = ''
		if(len(lst_con)!=0):
			for i in lst_con:
				s+=i+'\n'
		print(s)								
		return s	

	def getAddr(smg):
		if(isAddr(smg)):
			lt = smg.split('$')
			return lt[1]

	def isAddr(smg):
		if(smg.count('$')):
			lt = smg.split('$')
			if(len(lst_con)!=0 & lst_con.count(lt[1])==1):
				return True

		return False
		

	def scmd(cmd,acc,addr):
		if(cmd==1):
			acc.send(bytes('send file... ready to recieve..','ascii'))

				# Three thing to receive

			fname = (acc.recv(1024)).decode()
			length = int((acc.recv(1024)).decode())
			data = ''
			for x in range(length):
				tmp = (acc.recv(1024)).decode()
				data = '\n'+tmp
			with file(fname,'w') as fs:
				fs.write(data)
		acc.send(bytes('successfully transfered data','ascii'))

	def Process(acc,addr):
		try:
			smg = (acc.recv(1024)).decode()

			print('from {0},{1} : {2}'.format(lst_con.index(str(addr)),addr,smg))		

			if(isAddr(smg)):
				acc.send(bytes('Not ready yet...','ascii'))
				Process(acc,addr)

		# main2 branch feature
			if(smg=='get_cons'):
				acc.send(bytes(getCons(),'ascii'))
				Process(acc,addr)
			
			if(smg=='exiT0'):
				print('exit request...')
				acc.send(bytes('Exit req. received..\nYou can type any to close now......','ascii'))
				raise Exception('disconnecting with client...')

				
			acc.send(bytes(smg.upper(),'ascii'))
			Process(acc,addr)

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			print(f'Handler : {e}')
			print('Connection lost from {0} on process {1} line {2}'.format(addr,os.getpid(),exc_tb.tb_lineno))
			acc.close()
			print('Remote conneciton closed...')
			if(lst_con.count(str(addr))):
				lst_con.remove(str(addr))				

			

	while(True):
		acc,addr = s.accept()
		print('Connection from : {0}'.format(addr))
		acc.send(bytes(f'You : {addr} \n {cmd}','ascii')) #main2
		lst_con.append(str(addr))
		thread = threading.Thread(target=Process,args=(acc,addr,))
		thread.daemon = True
		thread.start()

except OSError as e:
	s.close()
	print('{0} : {1}'.format(type(e),e))
	s = 0



