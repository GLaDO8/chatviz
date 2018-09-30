import importer
import data_parser
import matplotlib.pyplot as plt

# open text file
chat = importer.chat_import("/Users/glados/Documents/test_data.txt")

chat_tstamp = data_parser.parse_chat(chat)

def plt_tseries_len(chat_tstamp):