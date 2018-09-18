test_no = int(input(''))
A = {}
B = {}
try:
    if(test_no > 0 and test_no < 5):
        for i in range(test_no):
            no = int(input(''))
            for j in range(no):
                set1 = input()
                setA = int(set1.split(' '))
                set2 = input()
                setB = int(set2.split(' '))
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
