import os 

class FileProp:

	def __init__(self,fnsz,file,fname,size):
		self.file = file
		self.fname = fname
		self.size = size
		self.fnsz = fnsz

def check(smg):
	if(smg.count('$')):
		if((smg.split('$'))[0]=='reqPath10004'):
			return True
	
	return False			


def getLsts(pa):
	try:
		print('->into processor')
		file = 0
		if(os.path.exists(pa)):
			file = open(pa,'rb')
			lst = file.read()
			print('->read completed...')
		else:
			return 0

		fname = (pa.split('\\'))[len(pa.split('\\'))-1]
		sz = str(len(lst))
		fnsz = f'{fname}${sz}'

		return FileProp(fnsz,file,fname,sz)
	except Exception as e:
		raise e
	
	
	

	
