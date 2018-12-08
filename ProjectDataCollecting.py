import time
import json
import re
import os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

C_KEY = ''
C_SECRET = ''
A_TOKEN_KEY = ''
A_TOKEN_SECRET = ''

class MyListener(StreamListener):

    def __init__(self, time_limit=30):
        self.start_time = time.time()
        self.limit = time_limit
        self.outFile = open('naturaldisaster.json', 'a',encoding = 'utf-8')
        super(MyListener, self).__init__()
    
    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            data = json.loads(data)
            if "coordinates" in data:
                if data["coordinates"] != None:
                    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
                    prestring = data['text'].replace('\n', ' ')
                    final_string = prestring.encode("UTF-8", 'ignore');
                    result = '{"text":"'+data['text']+'","created_at":"'+data['created_at']+'",'+'"coordinates":"['+str(data['coordinates']['coordinates'][0])+','+str(data['coordinates']['coordinates'][1])+']"},'
                    final_result = emoji_pattern.sub(r'', result)
                    self.outFile.write(final_result)
                    self.outFile.write('\n')
                    self.outFile.flush()
                    return True
        else:
            self.outFile.close()
            return False

    def on_error(self, status):
        print(status)

auth = OAuthHandler(C_KEY,C_SECRET)
auth.set_access_token(A_TOKEN_KEY,A_TOKEN_SECRET)
myStream = Stream(auth,MyListener(time_limit=3196800))
try:
    myStream.filter(track=['wild fire','earthquake','tornado','flood''volcanic eruption','thunderstorm','hailstorm'])
except:
    pass
