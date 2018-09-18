#print "Hello world"
#hello
#print" My name is Khan"
#fname=raw_input('Enter first name: ')
#lname=raw_input('Enter second name : ')

#print ('This is the name : %s %s' %(fname,lname))
#print("First value :"+str(s)+"second value"+str(b))
#print(type(s))
#fullname=raw_input('Enter the full name: ')
#age=raw_input('Enter age: ')
#age=int(age)
#firstname,lastname=fullname.split(' ')
#print ("The first name is %s, the second name is %s, the age is %s" %(firstname,lastname,age))
"""if(age>=18):
	print('Eligible for voting')
else:
	print('Not eligible for voting')"""

"""date=raw_input("Enter birthday with/:")
date1=date.split('/')
d0=int(date1[0])
d1=int(date1[1])
d2=int(date1[2])
print d1,d2,d0
sum=0
sum1=0
sum=d0+d1+d2
print sum
while(sum>0):
	dig=sum%10
	sum1=sum1+dig
	sum=sum//10
print ("The numerology number is : %s" %sum1)
"""
	

"""a=int(raw_input('Enter number 1 : '))
b=int(raw_input('Enter number 2 : '))
c=int(raw_input('Enter number 3 : '))
if(a==b or a==c or b==c):
	print "0"
else:
	sum=a+b+c
	print "The sum is %s" %sum"""
	
"""a=[5,10,20]
b=10
c=15
if(c in a):
	print(b)
elif(a not b):
	print(c)
else:
	print(a)"""
	
"""'''sd'''a=''
if a:
	print(a)
else:
	print("Die hey")"""
	
"""a=[1,2,3,4,5,6,7,8]
for i in a:
	b=8
	if(i%2==0):
		print(i)
print b"""

"""c=range(100)
for i in c:
	if(i%2==0):
		print ("Even %s" %i)
for i2 in c:
	if not (i2%2==0):
		print("Odd %s" %i2)"""

"""c=range(100)
odd=[]
even=[]
i=0
while(i<101):
	if not (i%2==0):
		odd.append(i)
	else:
		even.append(i)
print (odd,even)"""

"""year=int(raw_input('Enter year : '))
if(year%4==0):
	print('Leap year')
else:
	print('Not a leap year')"""
	
"""st=raw_input('Enter the string : ')
u=l=0
for i in st:
	if i.isupper():
		u+=1
	elif i.islower():
		l+=1
	else:
		pass
print("The number of upper case characters is : %s" %u)
print("The number of lower case characters is : %s" %l)"""

"""li=[]
n=int(raw_input('Enter the number of numbers:'))
sum=0
for num in range(n):
	nu1=int(raw_input('Enter number :'))
	if nu1%2==0:
		li.append(nu1)
for i in li:
	if(i%2==0):
		print(i)
		sum=sum+i
	else:
		pass
print("The sum of even numbers is : %s"%sum)"""

"""pw=raw_input('Enter the password :')
fl1=fl2=fl3=fl4=0
for i in pw:
	if i.isupper():
		fl1=fl1+1
	elif i.islower():
		fl2=fl2+1
	elif i.isdigit():
		fl3=fl3+1
	else:
		fl4=fl4+1
if((fl1>=1) and (fl2>=1) and (fl3>=1) and(fl4>=1)):
	print("Password is strong")
else:
	print("Password is weak")"""
	
"""thisdict =	{"brand": ["Ford","Renault"],"model": ["Mustang","Scavera"],"year": [1964,2006]}
thisdict['Sales']=[50,50]
print(thisdict["Sales"])
for x, y in thisdict.items():
  print(x, thisdict[x])
for x in thisdict.keys():
  print(x,thisdict[x])"""
  
"""employee={'name':'Sri','skill':{'python':5,'Agile':5,'Git':5}}
for k,v in employee.items():
	print(k,v)
	if(isinstance(v,dict)):
		for k1,v1 in v.items():
			print k1,v1"""

"""employee={'name':'Sri','skill':['python','Agile','Git']}
for k in employee.items():
	print(k)"""
	
	
