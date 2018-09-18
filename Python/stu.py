student={}
stud_count=raw_input("enter the no of students")
#n=2
#student=dict(raw_input().split() for _ in range(n))
for i in range(int(stud_count)):
    stud_name=raw_input("enter the name")
    stud_subcount=raw_input("enter the no of subjects")
    m_list=[]
    for j in range(int(stud_subcount)):
        j=j+1
        marks=int(input("enter the marks for the subject"+str(j)+":"))
        m_list.append(marks)
        student[stud_name]=m_list
print student
name=raw_input("enter the name")
if name in student:
    sum1=sum(student[stud_name])
    av1=sum1/3
    print(name)
    print(av1)
#def add_fn():
    #student={'student1':[100,80,40],'student2':[40,50,60]}
    #print(student)
    #sum1=student['student1'][0]+student['student1'][1]+student['student1'][2]
    #avg1=sum1/3
    #sum2=student['student2'][0]+student['student2'][1]+student['student2'][2]
    #avg2=sum2/3
    #student1=raw_input("enter the marks")
    #sum1=sum(student['student1'])
    #sum2=sum(student['student2'])
    #av1=sum1/3
    #av2=sum2/3
    #return sum1,sum2,av1,av2
#s=add_fn()
#print(s)




try:
  dict={}
  n=input("Enter the no of test case")
  for i in range(n):
      s=raw_input("Enter a and b");
      l1=s.split(" ")
      dict[i]=l1
  for i in range(n):
      print int(dict[i][0])/int(dict[i][1])
  #print dict
except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero")
except ValueError,Argument:
    print("Error Code: invalid literal for int() with base 10:%s"%l[1])
   