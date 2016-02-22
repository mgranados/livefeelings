import tweepy, time, sys, signal
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '#'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '#'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '#'#keep the quotes, replace this with your access token
ACCESS_SECRET = '#'#keep the quotes, replace this with your access token secret


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#erase tweets
file = open('tweets1.txt', 'w+')
file.close()

mex = [-111.88,15.98,-89.34,29.44]
ny = [-74,40,-73,41]
sf = [-122.75,36.8,-121.75,37.8]
points =[]
timer = 90

if sys.argv[1] == "ny":
    points = ny
    timer = 270
elif sys.argv[1] == "sf":
    points = sf
    timer = 200
elif sys.argv[1] == "mex":
    points = mex
    timer = 180

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if status == 420:
            #returning False in on_data disconnects the stream
            return False

if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


    stream = Stream(auth, l)
    # Mex location should rotate
    stream.filter(locations=points, async=True)
    signal.alarm(timer) #seconds
