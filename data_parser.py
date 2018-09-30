import helperfunctions

#segregate raw .txt file into a nested dict structure with JSON-like referencing
def parse_chat(chat):
    sender_dict_tstamp = {}
    for lines in chat.readlines():
        time_index = lines.find("-")
        if(helperfunctions.is_date(lines[:time_index])):
            colon_index = lines[time_index+2:].find(":")
            name_tstamp = lines[time_index+2:colon_index+time_index+2]   
            if(name_tstamp in sender_dict_tstamp.keys()):
                if (lines[:time_index] in sender_dict_tstamp[name_tstamp].keys()):
                    sender_dict_tstamp[name_tstamp][lines[:time_index]].append(lines[colon_index+time_index+4:])
                else:
                    sender_dict_tstamp[name_tstamp][lines[:time_index]] = list()
                    sender_dict_tstamp[name_tstamp][lines[:time_index]].append(lines[colon_index+time_index+4:])
            else:
                sender_dict_tstamp[name_tstamp] = dict()
                sender_dict_tstamp[name_tstamp][lines[:time_index]] = list()
                sender_dict_tstamp[name_tstamp][lines[:time_index]].append(lines[colon_index+time_index+4:])
    return sender_dict_tstamp 
