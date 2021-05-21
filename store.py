#python 3
#simple script to check items in list
#version 1.0 using List
#by safou abderrahim

products = ["watchs","shoes","jackets","jeanes","hats"] 

print("This is our products.choose one.")

c=0
for i in products:
	c+=1
	print("%d-%s"%(c,i))
	
coustumer_chois = input("what are you looking for?:")



if coustumer_chois in products:
	print("yes sir there is %s for you! visit our store to check the price\
	https:\\\www.ClStore.com\\%s"%(coustumer_chois,coustumer_chois))
	
else:
	print("sorry we dont have %s"%(coustumer_chois))