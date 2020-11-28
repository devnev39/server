import os 

lst = 0

path = 'C:\\Users\\Home\\Desktop\\Flute Fl Record.mp3'

if(os.path.exists(path)):
	
	with open(path,'rb') as file:
		lst = file.read()
		print(len(lst))
		print(type(lst))

else:
	print('it dont')

print(type(lst))

with open('test.mp3','wb') as file:
	file.write(lst)
	print('finished writing...')



lst = bytes('This is for test','ascii')
print(type(lst))
