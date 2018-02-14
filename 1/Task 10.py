#TASK 10 COMPLETE

import json
from pattern.en import sentiment
import os

a = open('CrimeReport.txt').readlines()

#print(a)

tweets = list()
t = []
f = []

for i in range(0, len(a)):
    tweets.append(json.loads(a[i]))

def positive(s, threshold = 0.1):
    (pol, sub) = sentiment(s)
    #print (pol)
    if(pol >= threshold):
        return True
    else:
        return False

for i in range(0, len(tweets)):
    b = positive(tweets[i]['text'])
    #print b
    if (b == True):
        t.append(tweets[i])
    else:
        f.append(tweets[i])

#print t
#print f

path = "/Users/Jinal/PycharmProjects/HW 1 B/Task 10/"

if not os.path.exists(path):
    os.makedirs(path)

file_name1 = 'Positive_Sentiment_Tweets.txt'
with open (os.path.join(path, file_name1), 'w') as f1:
    f1.write(str(t))

file_name2 = 'Negative_Sentiment_Tweets.txt'
with open (os.path.join(path, file_name2), 'w') as f2:
    f2.write(str(f))
