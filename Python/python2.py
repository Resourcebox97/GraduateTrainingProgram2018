"""inventory = {'gold' : 500,'pouch' : ['flint', 'twine', 'gemstone'],'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}
def fn1():
	inventory['pocket']=[]
	inventory['pocket']=['seashell','strange berry','list']
	print(inventory)
def fn2():
	#inventory = {'gold' : 500,'pouch' : ['flint', 'twine', 'gemstone'],'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}
	inventory['backpack'].sort()
	print(inventory['backpack'])
	inventory['backpack'].remove('dagger')
	print(inventory['backpack'])
def fn3():
	#inventory = {'gold' : 500,'pouch' : ['flint', 'twine', 'gemstone'],'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}
	inventory['gold']+=50
	print(inventory['gold'])
fn1()
fn2()
fn3()"""

"""key2=raw_input('Enter the second key : ')
		n2=raw_input('Enter the number of values in the first key : ')
		print("Enter the marks :")
		for j in range(n2):	
		for j in range(n2):	
			mark2=int(raw_input())
			m1.append(mark2)"""

"""

def fn4():
	student={}
	no=int(raw_input('Enter the number of keys : '))
	m1=m2=ke=[]
	for k in range(no):
		key_name=raw_input('Enter the key name: ')
		n=int(raw_input('Enter the number of values in the %s key : ' %key_name))
		print("Enter the marks :")
		for i in range(n):	
			mark1=int(raw_input())
			m1.append(mark1)
	for j in range(no):
		student[key_name]=m1
		total1=sum(student[key_name])
		avg1=total1/len(student[key_name])
		print("The name is %s and his marks, average of student1 are %s %s" %(key_name,total1,avg1))
		#print(student)
fn4()
"""

test_no=int(input(''))
A={}
B={}
try:
    if(test_no>0 and test_no<5):
        for i in range(test_no):
            no=int(input(''))
            for j in range(no):
                set1=input()
                setA=int(set1.split(' '))
                set2=input()
                setB=int(set2.split(' '))
                if(len(setA) > 0 and len(setA) < 10):
                    for k in range(len(setA)):
                        A.add(setA[k])
                else:
                    print('Enter 1-9 values for a set')
                if (len(setB) > 0 and len(setB) < 10):
                    for k in range(len(setB)):
                        B.add(setB[k])
                else:
                    print('Enter 1-9 values for a set')
            if(A.issubset(B)):
                print('True')
            else:
                print('False')
    else:
        print('Enter 1-4 testcases')
except Exception as err:
    print(err)
