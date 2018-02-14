# Download Data from Twitter

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "834430520834588672-rfdIs9Wy4Rk1VCoUItnBsNrDAq1aB7u"
access_token_secret = "XSTdVYqlyMclmKnJjhvqJFIOZ9XRgZBesVQxBQBDqYPxN"
consumer_key = "Tuiw8om8n8s19moC83kM6KCkQ"
consumer_secret = "JdMI8puIbKEJgnY0cG3npVgsNp0VgWLNHpYwQ60HdYLYD3AoKX"


class StdOutListener(StreamListener):

    def on_data(self, data):
        c = data
        b = ''
        print(c)
        b += c
        #print(b)
        f = open('Random_Data.txt', 'a')
        f.write(b)

        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['english'])
