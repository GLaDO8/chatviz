import importer
import helperfunctions

# open text file
chat = importer.chat_import("/Users/glados/Documents/test_data.txt")

#segregate raw .txt file into individual texts
def chat_parser(chat):
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

chat_tstamp = chat_parser(chat)       
#print (chat_tstamp["shreyas Gupta"]) 

