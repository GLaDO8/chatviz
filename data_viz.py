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
    colors = ['r', 'g', 'b']
    for i, key in enumerate(chat_tstamp.keys(), 0):
        temp = []
        for texts in chat_tstamp[key].values():
            temp.append(texts[0])
        plt.plot(chat_tstamp[key].keys(), temp, colors[i])
    plt.show()
        # count = 0
        # avg = [], mean_list1 = [], mean_list2 = []
        # for i, val in enumerate(chat_tstamp[key].keys(), 1):
        #     count = count+1
        #     if (count <=7 && i!=len(chat_tstamp[key].keys())):
        #         avg.append(val)
        #     else if(count>7):
        #         mean_list2.append(mean(avg))




if __name__ == "__main__":
    chat = importer.chat_import("/Users/glados/Documents/test_data.txt")
    chat_tstamp = data_parser.parse_chat(chat) 
    plt_tseries_len(chat_tstamp)
