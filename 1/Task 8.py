# TASK 8 COMPLETE

import json

import datetime

a = open('CrimeReport.txt').readlines()

#print(a)

tweets = list()

for i in range(0,len(a)):
    tweets.append(json.loads(a[i]))

#print(tweets)

sorted_tweets = sorted(tweets, key = lambda item: datetime.datetime.strptime(item['created_at'], "%a %b %d %X %z %Y"), reverse=True)
c = (sorted_tweets[0:10])
print (c)

f = open('task8.data', 'w')

for i in range(0, len(c)):
    f.write(json.dumps(c[i]) + '\n')

f.close()