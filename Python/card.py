"""#l=[1,2,3,4,5]
def square(n):
	return n**2
def cube(n):
	return n**3
#y=map(square,l)
funcs=[square,cube]
for i in range(5):
	value=map(lambda x:x(i),funcs)
	print value
#print(type(y))
#print (y)"""

import pandas as pd

df=pd.DataFrame(data=[1,2,'test',4,5])
#print df

df1=pd.DataFrame(data={'col1':[1,2,3],'col2':['a','b','c']})
#print df1
#print df1.dtypes
#print df.dtypes

df2=pd.DataFrame(data=df1)
#print df2

df1['col1']=[4,5,6]
#print df1
#print df1.columns
#print df1.values
df1.columns=['new','test']
print df1

df1['col3']=['val1','val2','val3']

print df1
