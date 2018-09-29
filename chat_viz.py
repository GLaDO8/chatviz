import importer
import helperfunctions

# open text file
chat = importer.chat_import("/Users/glados/Documents/test_data.txt")

#segregate raw .txt file into individual texts
def chat_parser(chat):
    chat_tstamp = []
    for lines in chat.readlines():
        comm_index = lines.find("-")
        if(helperfunctions.is_date(lines[:comm_index])):
            chat_tstamp.append(lines)
    return chat_tstamp 

chat_tstamp = chat_parser(chat)       
# print (chat_tstamp) 
def sender_dict_create(parsed_chat) #create nested dicts
    sender_dict_tstamp = {}
    for line in parsed_chat:
        time_index = line.find("-")
        #helperfunctions.parse_datetime(line[:time_index])
        colon_index = line[time_index+2:].find(':')
        name_tstamp = line[time_index+2:colon_index+time_index+2]
        sender_dict_tstamp[name_tstamp] = line
#print(sender_dict_tstamp.keys())
sender_dict_tstamp = sender_dict_create(chat_tstamp)
