import helperfunctions
from collections import defaultdict

#segregate raw .txt file into a nested dict structure
def parse_chat(chat):
    sender_dict_tstamp = {}
    for lines in chat.readlines():
        time_index = lines.find("-")
        if(helperfunctions.is_date(lines[:time_index])):
            colon_index = lines[time_index+2:].find(":")
            name_tstamp = lines[time_index+2:colon_index+time_index+2]   
            if(name_tstamp in sender_dict_tstamp.keys()):
                sender_dict_tstamp[name_tstamp].append(lines)
            else:
                sender_dict_tstamp[name_tstamp] = list(lines)
    return sender_dict_tstamp 
