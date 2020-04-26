from lxml import etree
from collections import Counter
import pandas as pd



tree = etree.parse("FoodServicesData.xml")
result_type=tree.xpath('//TypeDescription')
root = tree.getroot()
# I can't do it in this way.....

###(2)
df1 = []
for i in root.iter("TypeDescription"):
        df1.append(i.text)

result = Counter(df1)
result = pd.DataFrame.from_dict(result, orient='index').reset_index()
result.columns = ["type","count"]
result = result.sort_values(by="type", ascending=True).reset_index(drop=True)
result = result.iloc[:,:].values


for i in range(1,21):
    print(result[i,0]," ", result[i,1])


###(3)
df2 = []
for i in root.iter("Grade"):
        df2.append(i.text)

result2 = Counter(df2)
result2 = pd.DataFrame.from_dict(result2, orient='index').reset_index()
result2.columns = ["type","count"]
result2 = result2.sort_values(by="type", ascending=True).reset_index(drop=True)
result2 = result2.iloc[:,:].values


for i in range(0,4):
    print(result2[i,0]," ", result2[i,1])