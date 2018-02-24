import tweepy
import os
import time
import traceback
import sys

class auth:
    # 各種キー設定
    def __init__(self,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_SECRET = ACCESS_SECRET
    def get_auth():
        # authを生成
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY,self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN,self.ACCESS_SECRET)
        return  tweepy.API(auth)

# 継承
class MyStreamListener(tweepy.StreamListener):
#    def __init__(self):
#        super(StreamListener,self).__init__()
    def on_status(self,status):
        print(status.text)
        return True
    def on_error(self,status_code):
        print("取得失敗" + str(status_code))
        return True
    def on_timeout(self):
        print("タイムアウト")
        return True

if __name__ == '__main__':
    # キーの設定(あとでファイルから読み込み様に変更しておく)
    CONSUMER_KEY = 'xKAQknEYTCf0nMGLeGqhaAodn'
    CONSUMER_SECRET = 'PKnu4QHpmWq2E2o50IEOgnJ1KHmwzbvAzXr1eG1wgeb1V70ROU'
    ACCESS_TOKEN ='812559989176836097-gkq8XpaqeGT3FmedH0MHqVygfHjLicx'
    ACCESS_SECRET = 'JuofNQjgM2bkpGbhILZ64yqJgELTnwBgwLvgVgwg1dL11'


    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
#    api = tweepy.API(auth)
#    au = auth(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)

    
    # 接続確認
    try:
        api = tweepy.API(auth)
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    except:
        print("api接続失敗しました")
        print(traceback.format_exc())
        sys.exit()

    # 取得開始
    while True:
        try:
            print("ストリーム取得開始")
            myStream.filter(track=['python']) 
        except:
            # 失敗したら1分後に再接続
            print("ストリーム接続失敗")
            print(traceback.format_exc())
            time.sleep(30)
            system = tweepy.Stream(api.auth,StreamListener())

