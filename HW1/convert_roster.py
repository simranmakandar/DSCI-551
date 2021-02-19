import re
import json
import sys

commandArgs = sys.argv

with open(commandArgs[1], 'r') as f:
    with open("task2b.csv", 'w') as f1:
        next(f)  # skip header line
        for line in f:
            f1.write(line)

file4 = open("task2b.csv", 'r')
final_use3 = []
for f in file4:
    a = f.replace('"', '')
    x = re.split(",", a, 2)
    #     print(x)
    usable = [i.replace('\n', '') for i in x]
    #     print(usable)
    usable[0], usable[1] = usable[1], usable[0]
    #     print(usable)
    usable1 = [usable[0] + " " + usable[1], usable[-1]]
    #     print(usable1)
    usable2 = [num.lstrip() for num in usable1]
    final_use3.append({'Name': usable2[0], 'Participating from': usable2[-1]})

# print(final_use3)
final_json_data2b = json.dumps(final_use3)
with open(commandArgs[2], "w") as output2b:
    output2b.write(final_json_data2b)
