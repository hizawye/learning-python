'''python 3
author => safou abderrahim
istagram account => @just.rahim
script goal-> \' creating algerian random phone numbers \' '''
from random import randint

number_list = []

def getPhnum(sim_num):
	''''a function to creat random list with random numbers and take the argument  from the user and make everything together'''
	for _ in range(8) :
		rand_number = randint(0,9)
		number_list.append(rand_number)
	
	if sim_num == 1 :
		return '07'+"".join(map(str,number_list))
	elif sim_num == 2 :
		return '05'+''.join(map(str ,number_list))
	elif sim_num == 3 :
		return '06'+''.join(map(str , number_list))
	else :
		return '[×!] Wrong input'

pn = 'phone number'
print ('''-Generating random algerian phone number-
[1] Djezzy {0}
[2] Ooredo {0}
[3] mobilis {0}
'''.format(pn))

count = 1

while True :
	user_choice = int (input ('choose one of the above :'))
	print ('number({0})>> '.format(count),getPhnum(user_choice))

	number_list.clear()

	count += 1