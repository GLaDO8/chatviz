import importer
import data_parser
import matplotlib.pyplot as plt
# open text file

def plt_tseries_len(chat_tstamp):
    for key in chat_tstamp.keys():
        for tstamp in chat_tstamp[key].keys():
            for texts in chat_tstamp[key][tstamp]:
                text_len = 0
                for text in texts:
                    text_len = text_len + len(text)
            chat_tstamp[key][tstamp].insert(0, text_len)
    
    for key in chat_tstamp.keys():
        temp = []
        for texts in chat_tstamp[key].values():
            temp.append(texts[0])
        # plt.plot(tuple(chat_tstamp[key].keys()), tuple(temp))
        # plt.show()
if __name__ == "__main__":
    chat = importer.chat_import("/Users/glados/Documents/test_data.txt")
    chat_tstamp = data_parser.parse_chat(chat) 
    plt_tseries_len(chat_tstamp)
