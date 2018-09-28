import matplotlib.pyplot as plt
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

# open text file
chat = open("/Users/glados/Documents/glaDOS\ Archives/test_data.txt", "r+")

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

sender_dict_tstamp = {}
for line in chat_tstamp:
    time_index = line.find("-")
    colon_index = line[time_index+2:].find(':')
    name_tstamp = line[time_index+2:colon_index+time_index+2]
    sender_dict_tstamp[name_tstamp] = line
