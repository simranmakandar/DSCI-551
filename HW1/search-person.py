import re
import pandas as pd
import json
import sys
import requests

commandArgs = sys.argv
a = str(commandArgs[1]).lower()
# requests.put('https://dsci551-2-default-rtdb.firebaseio.com/.json', data = final_use3_json)
gotthis = requests.get('https://dsci551-2-default-rtdb.firebaseio.com/.json')
data1 = gotthis.json()
df = pd.DataFrame.from_dict(data1, orient='columns')
df['Name'] = df['Name'].str.lower()
df1 = df['Name'].tolist()

for name in df1:
    if a in str(name).split():
        print(name)
