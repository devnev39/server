import os 
import math
def check(smg):
	if(smg.count('$')):
		if((smg.split('$'))[0]=='reqPath10004'):
			return True
	
	return False			


def sendFile(pa,sck):
	try:
		PACK_SIZE = 1500 #1024 bytes at a time 
		with open(pa,'rb') as file:
			print('reading file..')
			data = file.read()
			fname = (pa.split('//'))[(len(pa.split('//')))-1]
			size = len(data)
			packets = 1
			remains = 0
			if(size>1024):
				packets = math.floor(size/PACK_SIZE)
				remains = size - (packets*PACK_SIZE)
				packets+=1
			fnsz = f'{fname}${size}${packets}${PACK_SIZE}${remains}'
			print(f'File : {fname} size : {size} packets : {packets} packsize : {PACK_SIZE} reamins : {remains}')
			sck.send(bytes(fnsz,'ascii'))				
			file.seek(0)
			sent = 0
			for x in range(packets):
				if(x==(packets-1) & remains!=0):
					data = file.read(remains)
					sck.send(data)
					print('last sent...') 				
				data = file.read(PACK_SIZE)
				sck.send(PACK_SIZE)
				sent += PACK_SIZE
				print(f'{(x*100)/size} % sent')
			print('file sent....')	


	except Exception as e:
		raise e
	
	
	

	
