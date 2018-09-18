import csv
import pandas as pd
#with open('chipotle.tsv') as tsvfile:
  #chipo = csv.DictReader(tsvfile, dialect='excel-tab')
  #for row in chipo:
    #print(row)
chipo1=pd.read_csv('chipotle.tsv',sep='\t')
#print chipo1
df=chipo1[['item_name','item_price']]
#print df['item_price']
result=chipo1.sort_values(['item_name'],ascending=[0])
#print result
res=chipo1
#print res
res['item_price']=res.item_price.str.split('$')
print(res['item_price'].max())
#count=chipo1.loc['Veggie Salad Bowl'].count()
#print count