from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):
    
    def on_data