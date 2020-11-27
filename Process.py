import os
import sys

def getCons(lst_con):
	s = ''
	if(len(lst_con)!=0):
		for i in lst_con:
			s+=i+'\n'
	print(s)								
	return s

def isAddr(smg):

	if(smg.count('$')):
		lt = smg.split('$')
		if(len(lst_con)!=0 & lst_con.count(lt[1])==1):
			return True

	return False
def process(acc,addr,lst_con):
	try:

		smg = (acc.recv(1024)).decode()
		print('from {0},{1} : {2}'.format(lst_con.index(str(addr)),addr,smg))		

		if(isAddr(smg)):
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
		exc_type, exc_obj, exc_tb = sys.exc_info()
		print(f'Handler : {e}')
		print('Connection lost from {0} on process {1} line {2}'.format(addr,os.getpid(),exc_tb.tb_lineno))
		acc.close()
		print('Remote conneciton closed...')
		if(lst_con.count(str(addr))):
			lst_con.remove(str(addr))				