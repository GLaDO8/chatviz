import importer
import helperfunctions

# open text file
chat = importer.chat_import("/Users/glados/Documents/test_data.txt")

#function to check if string is date


#segregate raw .txt file into individual texts
chat_tstamp = []
for lines in chat.readlines():
    comm_index = lines.find("-")
    if(helperfunctions.is_date(lines[:comm_index])):
        chat_tstamp.append(lines)
# print (chat_tstamp)

sender_dict_tstamp = {}
for line in chat_tstamp:
    time_index = line.find("-")
    colon_index = line[time_index+2:].find(':')
    name_tstamp = line[time_index+2:colon_index+time_index+2]
    sender_dict_tstamp[name_tstamp] = line

print(sender_dict_tstamp.keys())
