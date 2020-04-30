from lxml import etree,html
import pandas as pd
import numpy as np


tree = html.parse("Browse | New & Used Books from ThriftBooks1.html")

# title
title= tree.xpath("/html/body//div[@class='AllEditionsItem-tileTitle']/a")
list_title=[]
for i in title:
   list_title.append(i.text)

# author
list_author=[]
author = tree.xpath('//div[@class="SearchResultListItem-bottomSpacing SearchResultListItem-subheading"]')

for i in author:
    if len(i) != 0:
        list_author.append(i.getchildren()[0].text)
    else:
        list_author.append("NA")


# price, condition and format
price = []
format = []
condition = []
pfc = tree.xpath('//div[@class="SearchResultTileItem-dataPoints"]')

for i in pfc:
    if len(i) !=1 :
        price.append(i.getchildren()[0].getchildren()[0].getchildren()[1].text)
        format.append(i.getchildren()[1].getchildren()[0].getchildren()[0].text_content())
        condition.append(i.getchildren()[1].getchildren()[1].getchildren()[1].text)
    else:
        price.append("NA")
        format.append("NA")
        condition.append("NA")



Data= pd.DataFrame([list_title,list_author,price,condition,format]).T
Data.columns = ['Title','Author','Price','Condition','Format']

root = etree.Element('books')
headers = Data.columns.values.tolist()

for row in Data.values.tolist():
    data = etree.SubElement(root, "book")
    for col in range(len(headers)):
        node = etree.SubElement(data, headers[col]).text = str(row[col])



tree_out = (etree.tostring (root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))

with open(r'books.xml', 'wb') as f:
    f.write(tree_out)