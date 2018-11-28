import pandas as pd
import numpy as np
import emoji
import re
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='shreyas_gupta', api_key='tVmUJLZ1BZ9RzmE92Pyi')

def chat_import(filepath):
    chat = open(filepath, "r+")
    return chat

chat = chat_import("/Users/glados/Documents/test_data.txt")
arr = []
for lines in chat.readlines():
    if(re.search("([0-9]{1,}\/[0-9]{1,}\/[0-9]{1,}\, [0-9]{1,}\:[0-9]{1,} (AM|PM) \- )", lines)):
        arr.append(lines)
    else:
        arr[len(arr)-1] = arr[len(arr)-1] + lines
chat_data = np.asarray(arr)
raw_data = pd.DataFrame(data = chat_data, columns = ["text"])

raw_data.text = raw_data.text.apply(lambda x: re.sub("\n|\\n", " ", x))
raw_data["timestamp"] = raw_data.text.apply(lambda x: re.search("([0-9]{1,}\/[0-9]{1,}\/[0-9]{1,}\, [0-9]{1,}\:[0-9]{1,} (AM|PM))", x).group(1))
raw_data.text = raw_data.text.apply(lambda x: re.sub("([0-9]{1,}\/[0-9]{1,}\/[0-9]{1,}\, [0-9]{1,}\:[0-9]{1,} (AM|PM)) \- ","", x))
raw_data["sender"] = raw_data.text.apply(lambda x: x[:x.find(":")])
raw_data.text = raw_data.text.apply(lambda x: x[x.find(":")+2:])
raw_data["year"] = pd.to_datetime(raw_data['timestamp']).dt.year
raw_data["month"] = pd.to_datetime(raw_data['timestamp']).dt.month
raw_data["day"] = pd.to_datetime(raw_data['timestamp']).dt.day
raw_data["hour"] = pd.to_datetime(raw_data['timestamp']).dt.hour
raw_data["dayofweek"] = pd.to_datetime(raw_data['timestamp']).dt.dayofweek
raw_data["text_length"] = raw_data.text.apply(lambda x: len(x))
raw_data["gif/image/video"] = raw_data.text.apply(lambda x: 1 if (x.find("<Media omitted>") != -1) else 0)
raw_data['emojis'] = raw_data.text.apply(lambda x: ''.join(emo for emo in x if emo in emoji.UNICODE_EMOJI))
raw_data['no_emojis'] = raw_data.text.apply(lambda x: len(''.join(emo for emo in x if emo in emoji.UNICODE_EMOJI)))
raw_data.drop(columns = ["timestamp"])
