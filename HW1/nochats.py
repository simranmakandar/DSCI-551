#### no_chats.py
import pandas as pd
import re
import json
import sys

commandArgs = sys.argv
with open(commandArgs[1]) as infile, open('output1b.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

with open(commandArgs[2], 'r') as f:
    with open("updated_test1.csv", 'w') as f1:
        next(f)  # skip header line
        for line in f:
            f1.write(line)

file1try = open("output1b.txt", "r")
file2try = open("updated_test1.csv", 'r')
# print(file1try.read())

df1again = pd.read_csv("output1b.txt", sep='\t', header=None)
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

dict = {}
final_use2_again = []
for fline in file2try:

    a = fline.replace('"', '')
    x = re.split(",", a, 2)
    #     print(x)
    usable_again = [i.replace('\n', '') for i in x]
    #     print(usable)
    usable_again[0], usable_again[1] = usable_again[1], usable_again[0]
    #     x = re.sub(",", " ", str(usable), 1)
    usable1_again = [usable_again[0] + " " + usable_again[1], usable_again[-1]]
    usable2_again = [num.lstrip() for num in usable1_again]
    if usable2_again[0] not in keylist1:
        final_use2_again.append({'Name': usable2_again[0], 'Participating from': usable2_again[-1]})
    if str(usable2_again[1]) == "Unknown":
        final_use2_again.append({'Name': usable2_again[0], 'Participating from': usable2_again[-1]})
# print(final_use2_again)

final_using = json.dumps(final_use2_again)
with open(commandArgs[3], 'w') as finalout:
    finalout.write(final_using)

# print(finallistagain)
