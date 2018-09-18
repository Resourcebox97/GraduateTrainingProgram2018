import pandas as pd

raw_data1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
data1=pd.DataFrame(raw_data1)
raw_data2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
data2=pd.DataFrame(raw_data2)
raw_data3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
data3=pd.DataFrame(raw_data3)

print data1
print data2
print data3

all_data_row=pd.concat([data1,data2])
#all_data_row=pd.merge(data1,data2,how="outer")
print("two dataframes along rows")

print all_data_row

all_data_col=pd.concat([data1,data2],axis=1)

print("two dataframes along columns")
print all_data_col

df=pd.merge(all_data_row,data3)

print df


print("to Merge only the data that has the same 'subject_id' on both data1 and data2")

df1=pd.merge(data1,data2,how="inner" ,on='subject_id')
print df1

df2=pd.merge(data1,data2,how="outer",on='subject_id')

print("Merge all values in data1 and data2, with matching records from both sides where available")

print df2



