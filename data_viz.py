import importer
import data_parser
import matplotlib.pyplot as plt
import emoji

def make_features(raw_data):
    raw_data.text = raw_data.text.apply(lambda x: re.sub("\n|\\n", " ", x))
    raw_data["timestamp"] = raw_data.text.apply(lambda x: re.search("([0-9]{1,}\/[0-9]{1,}\/[0-9]{1,}\, [0-9]{1,}\:[0-9]{1,} (AM|PM))", x).group(1))
    raw_data.text = raw_data.text.apply(lambda x: re.sub("([0-9]{1,}\/[0-9]{1,}\/[0-9]{1,}\, [0-9]{1,}\:[0-9]{1,} (AM|PM)) \- ","", x))
    raw_data["sender"] = raw_data.text.apply(lambda x: x[:x.find(":")])
    raw_data.text = raw_data.text.apply(lambda x: x[x.find(":")+2:])
    raw_data["year"] = pd.to_datetime(raw_data['timestamp']).dt.year
    raw_data["month"] = pd.to_datetime(raw_data['timestamp']).dt.month
    raw_data["day"] = pd.to_datetime(raw_data['timestamp']).dt.day
    raw_data["hour"] = pd.to_datetime(raw_data['timestamp']).dt.hour
    raw_data["text_length"] = raw_data.text.apply(lambda x: len(x))
    raw_data["gif/image/video"] = raw_data.text.apply(lambda x: 1 if (x.find("<Media omitted>") != -1) else 0)
    raw_data['emojis'] = raw_data.text.apply(lambda x: ''.join(emo for emo in x if emo in emoji.UNICODE_EMOJI))
    raw_data['no_emojis'] = raw_data.text.apply(lambda x: len(''.join(emo for emo in x if emo in emoji.UNICODE_EMOJI)))
    return raw_data

if __name__ == "__main__":
    chat = importer.chat_import("/Users/glados/Documents/test_data.txt")
    raw_data = data_parser.parse_chat(chat) 
    pro_data = make_features(raw_data)
