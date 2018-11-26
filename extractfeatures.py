import importer
from data_parser import *
import emoji
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.tokenize import sent_tokenize, word_tokenize
def make_features(raw_data):
    raw_data.text = raw_data.text.apply(lambda x: re.sub("\n|\\n", " ", x))
    raw_data["timestamp"] = raw_data.text.apply(lambda x: re.search("([0-9]{1,}\/[0-9]{1,}\/[0-9]{1,}\, [0-9]{1,}\:[0-9]{1,} (AM|PM))", x).group(1))
    raw_data["year"] = pd.to_datetime(raw_data['timestamp']).dt.year
    raw_data["month"] = pd.to_datetime(raw_data['timestamp']).dt.month
    raw_data["day"] = pd.to_datetime(raw_data['timestamp']).dt.day
    raw_data["hour"] = pd.to_datetime(raw_data['timestamp']).dt.hour
    raw_data["dayofweek"] = pd.to_datetime(raw_data['timestamp']).dt.dayofweek
    raw_data["timestamp"] = pd.to_datetime(raw_data["timestamp"])
    raw_data.text = raw_data.text.apply(lambda x: re.sub("([0-9]{1,}\/[0-9]{1,}\/[0-9]{1,}\, [0-9]{1,}\:[0-9]{1,} (AM|PM)) \- ","", x))
    raw_data["sender"] = raw_data.text.apply(lambda x: x[:x.find(":")])
    raw_data.text = raw_data.text.apply(lambda x: x[x.find(":")+2:])
    raw_data["text_length"] = raw_data.text.apply(lambda x: len(x))
    raw_data["gif/image/video"] = raw_data.text.apply(lambda x: 1 if (x.find("<Media omitted>") != -1) else 0)
    raw_data['emojis'] = raw_data.text.apply(lambda x: ''.join(emo for emo in x if emo in emoji.UNICODE_EMOJI))
    raw_data['no_emojis'] = raw_data.text.apply(lambda x: len(''.join(emo for emo in x if emo in emoji.UNICODE_EMOJI)))
    raw_data["no of words"] = raw_data.text.apply(lambda x: len(word_tokenize(x)))
    raw_data["is_link"] = raw_data.text.apply(lambda x: 1 if (re.search("(https|http)\:\/\/", x)) else 0)
    return raw_data

def sentiment_analyser():
    

if __name__ == "__main__":
    chat = importer.chat_import("/Users/glados/Documents/test_data.txt")
    raw_data = parse_chat(chat) 
    pro_data = make_features(raw_data)