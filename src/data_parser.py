import helperfunctions
import importer
import numpy as np
import re 
import pandas as pd
#segregate raw .txt file into a nested dict structure with JSON-like referencing
def parse_chat(chat):
    arr = []
    for lines in chat.readlines():
        if(re.search("([0-9]{1,}\/[0-9]{1,}\/[0-9]{1,}\, [0-9]{1,}\:[0-9]{1,} (AM|PM) \- )", lines)):
            arr.append(lines)
        else:
            arr[len(arr)-1] = arr[len(arr)-1] + lines
    chat_data = np.asarray(arr)
    raw_data = pd.DataFrame(data = chat_data, columns = ["text"]) 
    return raw_data

if __name__ == "__main__":
    chat = importer.chat_import("/Users/glados/Documents/test_data.txt")
    
