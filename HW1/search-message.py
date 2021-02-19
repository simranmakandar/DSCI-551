import pandas as pd
import requests
import json
import sys

commandArgs = sys.argv
a = str(commandArgs[1]).lower()
b = str(commandArgs[2]).lower()
# print(a+" "+b)

# requests.put('https://dsci551-38120-default-rtdb.firebaseio.com/.json', data = result_mod_json)
fbx = requests.get('https://dsci551-38120-default-rtdb.firebaseio.com/.json')

data = fbx.json()
# print(data)
df = pd.DataFrame.from_dict(data, orient='columns')
df['Person'] = df['Person'].str.lower()
df1 = df.loc[df['Person'] == (a+" "+b)]
df2 = df1.drop(['Person'], axis = 1)
fileQ3 = df2.to_csv('task3.csv', sep ='\t')

fileQ3read = open('task3.csv','r')
print(fileQ3read.read())