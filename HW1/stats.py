######stats.py

import pandas as pd
# import re
import json
import sys

commandArgs = sys.argv

with open(commandArgs[1]) as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

file1try = open("output.txt", "r")
# print(file1try.read())

df1again = pd.read_csv("output.txt", sep='\t', header=None)
df1again.columns = ["Time", "Name", "Message"]
df1again["Name"] = df1again["Name"].map(lambda x: x.rstrip(':'))
result1againlist = df1again.values.tolist()
# print(df1again)
# print(result1againlist)
keylist1 = []
finallistagain = []
for itm in result1againlist:
    keylist1.append(itm[1])
    d = {}
    [d.__setitem__(item, 1 + d.get(item, 0)) for item in keylist1]

for person in d:
    finallistagain.append({'Person': person, 'Message': d[person]})

final_json_data = json.dumps(finallistagain)
# print(final_json_data)

with open(commandArgs[2],'w') as outputfile:
    outputfile.write(final_json_data)
# print(finallistagain)