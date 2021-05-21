




zawji=[]
fardi=[]
for i in range(20):
	s=i%2
	if s==0:
		zawji.append(i)
	elif s!=0:
		fardi.append(i)
		
print('''
{0} this is azawjiya
{1} and this is alfardia
  '''.format(zawji,fardi))
		