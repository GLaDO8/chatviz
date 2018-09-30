import importer
import data_parser
import matplotlib.pyplot as plt
import numpy as np

# open text file
chat = importer.chat_import("/Users/glados/Documents/test_data.txt")

chat_tstamp = data_parser.parse_chat(chat)
# items = tuple(chat_tstamp["Sushma"].keys())
# print (items)
def plt_tseries_len(chat_tstamp):
    for key in chat_tstamp.keys():
        plt.plot(tuple(chat_tstamp[key].keys()), tuple(chat_tstamp[key].values()))
    plt.legend()
    plt.show()
plt_tseries_len(chat_tstamp)