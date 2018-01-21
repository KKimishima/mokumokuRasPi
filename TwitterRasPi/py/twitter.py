import tweepy
import os

# 各種キー設定
CONSUMER_KEY = 'xKAQknEYTCf0nMGLeGqhaAodn'
CONSUMER_SECRET = 'PKnu4QHpmWq2E2o50IEOgnJ1KHmwzbvAzXr1eG1wgeb1V70ROU'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)

ACCESS_TOKEN ='812559989176836097-gkq8XpaqeGT3FmedH0MHqVygfHjLicx'
ACCESS_SECRET = 'JuofNQjgM2bkpGbhILZ64yqJgELTnwBgwLvgVgwg1dL11'

auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

#APIインスタンスを作製
api = tweepy.API(auth)
print("準備開始")

# つぶやきの取得
for status in tweepy.Cursor(api.user_timeline).items():
    tw_text = status.text
    print(tw_text)
    #os.system('path/to/jtalk.sh' + tw_text)
    break
