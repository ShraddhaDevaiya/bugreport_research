#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import re
import pandas as pd

pattern = \
    "(actual) | \s(agree) | (^agree) | (more) | (although) | (approach) | (attach) | \
      (because) |  \s(change) | (^change) | (create) | (document) | (duplicate) | (easy) | \s(far) | \
        (^far) |  \s(fix) | (^fix) | (for example) | (found\s) | (found:) | (however) | (I think) | \
          (implement) | (improve) | (in addition) | (in fact) | \s(include) | (^include) | \
            (instead) |  \s(just) | (^just) | (just\s) | (keep/s) | (kept) | (make) | (might) |   \s(miss) | \
              (^miss) | (need) | (option) | \s(other) | (^other) | (otherwise) | (patch) | \s(possible) | \
                (^possible) | (probably) |  \s(read) | (^read) | (read\s) | (reasonable) |   \s(resolve) | \
                  (^resolve) | (seem) |  \s(select) | (^select) | (since) | (solution) | (solve) |  \s(suggest) | \
                    (^suggest) | (support) | (therefore) | (want) | (whether) | (wonder) | (!wonderful) | (!workspace) | \
                      (work) |   \s(you can) | (you can\s) | (can you) | (you could)"
comment_list = []

plan_tag=[]

# Open file

with open('/mnt/c/Users/shrad/Documents/resea/TOBE/data/0_bugreport.csv'
          ) as file_obj:

    # Create reader object by passing the file
    # object to reader method

    reader_obj = csv.reader(file_obj)

    # Iterate over each row in the csv
    # file using reader object

    for row in reader_obj:
        comment_list.append(row)
        #print(comment_list)
        # match variable contains a Match object.
        match = re.search(pattern, str(row), flags=re.IGNORECASE) 
        if match:
          plan_tag.append(1)
        else:
          plan_tag.append(0)
print(len(plan_tag))
plabel_df = pd.DataFrame(plan_tag)
#print(plabel_df)

plabel_df.to_csv("/mnt/c/Users/shrad/Documents/resea/TOBE/data/plabel_list.csv")

