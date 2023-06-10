import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('/mnt/c/Users/shrad/Documents/resea/TOBE/data/bugreports.xml')
root=tree.getroot()
# print(tree)
# print([elem.tag for elem in root.iter()])

comment = []



for cm in root.iter('Sentence'):
  #print(cm.text)
  #print("step1")
  comment.append(cm.text)

#com_df = pd.DataFrame(list(zip(comment)))
com_df = pd.DataFrame(comment)
print(com_df)

com_df.to_csv("/mnt/c/Users/shrad/Documents/resea/TOBE/data/commment_list_sample.csv")