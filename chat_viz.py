import matplotlib.pyplot as plt
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

# open text file
chat = open("test_data.txt", "r+")

#function to check if string is date
def is_date(string):
    try: 
        parse(string)
        return True
    except ValueError:
        return False

#segregate raw .txt file into individual texts
chat_tstamp = []
for lines in chat.readlines():
    comm_index = lines.find("-")
    if(is_date(lines[:comm_index])):
        chat_tstamp.append(lines)
# print (chat_tstamp)

#create a list with no timestamps
chat_no_tstamp = []
for line in chat_tstamp:
    _del_index = line.find('-')
    chat_no_tstamp.append(line[_del_index+2:])
# print(chat_no_tstamp)

#create a dictionary with the sender name as dict keys
sender_dict = {}
for line in chat_no_tstamp:
    colon_index = line.find(':')
    name = line[:colon_index]
    sender_dict[name] = line[colon_index:]
# print(sender_dict.keys())