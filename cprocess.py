import os 

def check(smg):
	if(smg.count('$')):
		if((smg.split('$'))[0]=='reqPath10004'):
			return True
	
	return False			


def getLsts(pa):
	if(os.path.exists(pa)):
		lst = 0
		with open(pa,'rb') as file:
			lst = file.read()
	else:
		return 0
	fname = (pa.split('\\'))[len(pa.split('\\'))-1]
	sz = str(len(lst))
	return f'{fname}${sz}' , lst
	
