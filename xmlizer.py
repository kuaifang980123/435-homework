import pandas as pd
Data = pd.read_csv("FoodServiceData.csv")
from lxml import etree

root = etree.Element('FoodServices')
headers = Data.columns.values.tolist()

for row in Data.values.tolist():
    data = etree.SubElement(root, "foodservice")
    for col in range(len(headers)):
        node = etree.SubElement(data, headers[col]).text = str(row[col])




tree_out = (etree.tostring (root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))

with open(r'FoodServicesData.xml', 'wb') as f:
    f.write(tree_out)