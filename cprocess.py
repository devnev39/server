import os 

def check(smg):
	if(smg.count('$')):
		if((smg.split('$'))[0]=='reqPath10004'):
			return True
	
	return False			


def getLsts(path):
	if(os.path.exists(path)):
		lst = 0
		with open(path,'rb') as file:
			lst = file.read()
	else:
		return 0
	fname = (path.split('\\'))[len(path.split('\\'))-1]
	sz = len(lst)
	return f'{fname}${sz}' , lst
	
