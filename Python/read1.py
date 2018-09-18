
"""(1)
Full_name=raw_input("enter the full name")
lists=Full_name.split();
flag=-1
flag=Full_name.find(' ',0,len(Full_name))
print(type(flag))
if len(Full_name)<1000 and flag!=-1 :
	
	for i in range(len(lists)):
		if(lists[i].isalnum()):
			lists[i]=lists[i].capitalize()
	print(lists)	
print(" ".join(lists))

"""


"""(2)
d={}
count=raw_input("enter the no of students")
for i in range(int(count)):
	out=raw_input()
	lists=out.split(" ")
	keys=lists[0]
	sub_list=[]
	k=1
	
	for k in range(len(lists)):
		if k !=0 :
			sub=lists[k]
			sub_list.append(sub)
	d[keys]=sub_list
print(d)
name=raw_input("enter the name")
sum=0
for i in range(len(d[name])):
	sum=sum+int(d[name][i])
print(sum/len(d[name]))	
"""


"""(3)
def divide(a,b):
	try:
		c=a/b
		print c
	except Exception as e:
		print(e)
		
inp=input("enter the no of attempts")
for i in range(inp):
		a=raw_input()
		b=raw_input()
		divide(int(a),int(b))
		"""
		
		
(4)
lists=[]
def insert(index,value):
	lists.insert(index,value)
def prints():
	print(lists)
def removing(e):
	print(lists)
	lists.remove(e)
def appends(value):
	lists.append(value)
def sorting():
	lists.sort()
def poping():
	lists.pop()
def reversing():
	lists.reverse()
	
	
input=raw_input("enter the number of command operations")
for i in range(int(input)):
	out=raw_input()
	sub_list=out.split(" ")
	if(sub_list[0]=="insert"):
		insert(int(sub_list[1]),int(sub_list[2]))
	elif(sub_list[0]=="print"):	
		prints()
	elif(sub_list[0]=="remove"):
		print(int(sub_list[1]))
		removing(sub_list[1])
	elif(sub_list[0]=="append"):	
		appends(int(sub_list[1]))
	elif(sub_list[0]=="sort"):	
		sorting()
	elif(sub_list[0]=="pop"):	
		poping()
	elif(sub_list[0]=="reverse"):	
		reversing()		
	else:
		print("no operations")
print(lists)		