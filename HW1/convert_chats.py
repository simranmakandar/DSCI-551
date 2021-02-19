import pandas as pd
import sys
import json

commandArgs = sys.argv

with open(commandArgs[1]) as infile, open('task12a.csv', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

Cov = pd.read_csv("task12a.csv", sep='\t', header=None)
Cov.columns = ["Time", "Name", "Message"]
Cov["Name"] = Cov["Name"].map(lambda x: x.rstrip(':'))

result_list = Cov.values.tolist()
# print(result_list)
result_mod = []
for line in result_list:
    result_mod.append({"Time": str(line[0]), "Person": str(line[1]), "Message": str(line[2])})
#     print(result_mod)

result_mod_json = json.dumps(result_mod)
# print(result_mod)

with open(commandArgs[2], 'w') as output2a:
    output2a.write(result_mod_json)
