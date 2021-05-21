'''python 3
filling a lists by ranges.
==>by safou abderrahim
'''
zawji = []
fardi = []
def zawji_fardi (rang) :
	for i in range(rang) :
		s = i % 2
		if s == 0 and i != 0 :
			zawji.append(i)
		elif s !=0 :
			fardi.append(i)
	print ('''
	  %s this is alzawjiya
	  %s this is alfardia ''' % \
	   ( zawji, fardi ) )
	  
rg = int( input("Enter a range=>") )
zawji_fardi (rg)
