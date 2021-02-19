#####load.py

import requests
import json
import sys

commandArgs = sys.argv

data_file_chats = open(commandArgs[1],'r')
data_file_roster = open(commandArgs[2],'r')
requests.put('https://dsci551-38120-default-rtdb.firebaseio.com/.json', data = data_file_chats) #commandArgs[1]
requests.put('https://dsci551-2-default-rtdb.firebaseio.com/.json', data = data_file_roster) #commandArgs[2]
