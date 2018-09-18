"""name=raw_input('Enter the name : ')
if(len(name)>0 and len(name)<1000):
	name1=name.split()
	for i in range(len(name1)):
		#print('%s %s' %(name1[0].capitalize(),name1[1].capitalize()))
		if(name1[i].isalnum()):
			name1[i]=name1[i].capitalize()
print(" ".join(name1))"""


"""def fn4():
	student={}
	no=int(raw_input('Enter the number of students : '))
	m1=m2=ke=[]
	try:
		if(no>=2):
			for k in range(no):
				key_name=raw_input('Enter the student name: ')
				n=int(raw_input('Enter the number of marks for the student %s : ' %key_name))
				print("Enter the marks :")
				for i in range(n):	
					mark1=int(raw_input())
					if(mark1>=0 and mark1<=100):
						m1.append(mark1)
			for j in range(no):
				student[key_name]=m1
				total1=sum(student[key_name])
				avg1=total1/len(student[key_name])
			name=raw_input('Enter the name for retrieval : ')
			for l,k in student.items():
				if(l==name):
					print("The name is %s and his average is %.2f" %(l,avg1))
		#print(student)
	except Exception as err:
		print("Enter two or more details",err)
fn4()"""

"""class Shapes:
	def Circle_fn(self,r):
			area=3.14*r*r
			return area
	def Rectangle_fn(self,l,b):
			area1=l*b
			return area1
obj=Shapes()
r=int(raw_input('Enter the radius of circle : '))
try:
	if(r>0):
		area=obj.Circle_fn(r)
		print('The area is : %s'%area)
	else:
		print('Enter proper positive values')
except Exception as err:
	print('Enter a value greater 0',err)
l=int(raw_input('Enter the length of the rectangle : '))
b=int(raw_input('Enter the breadth of the rectangle : '))
try:
	if(l>0 and b>0):
		area1=obj.Rectangle_fn(l,b)
		print('The area is : %s'%area1)
	else:
		print('Enter proper positive values')
except Exception as err:
	print('Enter values greater than 0',err)"""
	
	
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
		removing(int(sub_list[1]))
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