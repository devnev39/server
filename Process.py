import os
import sys

def getCons(lst_con):
	s = ''
	if(len(lst_con)!=0):
		for i in lst_con:
			s+=i+'\n'
	print(s)								
	return s

def isAddr(smg,lst_con):

	if(smg.count('$')):
		lt = smg.split('$')
		if(len(lst_con)!=0 & lst_con.count(lt[1])==1):
			return True

	return False
def isWeb(smg):
	if(smg.count('\n')):
		ss = smg.split('\n')
		for s in ss:
			if(s=='GET / HTTP/1.1\r'):
				return True
	return False

def WebHandler(acc):
	print('web socket request.....')
	data = 'HTTP/1.1 200 OK\r\n'
	data+= 'Content-Type: text/html; charset=utf-8\r\n'
	data+= '\r\n'
	data+= '<html><title>Client</title><body><h1>Under Development...</body></html>\r\n\r\n'
	acc.sendall(data.encode())
	acc.close()

def process(acc,addr,lst_con):
	try:

		smg = (acc.recv(1024)).decode()
		print('from {0},{1} : {2}'.format(lst_con.index(str(addr)),addr,smg))		
		if(smg=='snd10004'):
			acc.send(bytes('reqPath10004$enter the path or file name : ','ascii'))
			resp = (acc.recv(1024)).decode()
			if(resp.count('$')):
				fname = (resp.split('$'))[0]
				size = int((resp.split('$'))[1])
				packets = int((resp.split('$'))[2])
				PACK_SIZE = int((resp.split('$'))[3])
				remains = int((resp.split('$'))[4])
				print(f'File : {fname} size : {size} packets : {packets} packsize : {PACK_SIZE} reamins : {remains}')
				received = 0
				with open(fname,'wb') as file:
					for x in range(packets):
						if(x==(packets-1) & remains!=0):
							data = acc.recv(remains)
							file.write(data)
							print('final pack received..')
						data = acc.recv(PACK_SIZE)
						file.write(data)
						received+=PACK_SIZE
						print(f'{(received*100)/size} % received..')
				print('received a file from {0}'.format(addr))	
				process(acc,addr,lst_con)								

				#this is to be done tommarrow

		if(isAddr(smg,lst_con)):
			acc.send(bytes('Not ready yet...','ascii'))
			process(acc,addr,lst_con)

		# main2 branch feature
		if(smg=='get_cons'):
			acc.send(bytes(getCons(lst_con),'ascii'))
			process(acc,addr,lst_con)
			
		if(smg=='exiT0'):
			print('exit request...')
			acc.send(bytes('Exit req. received..\nYou can type any to close now......','ascii'))
			raise Exception('disconnecting with client...')

				
		acc.send(bytes(smg.upper(),'ascii'))
		process(acc,addr,lst_con)

	except Exception as e:
		a, b, exc_tb = sys.exc_info()
		print(f'Handler : {e}')
		print('Connection lost from {0} on process {1} line {2}'.format(addr,os.getpid(),exc_tb.tb_lineno))
		acc.close()
		print('Remote conneciton closed...')
		if(lst_con.count(str(addr))):
			lst_con.remove(str(addr))				