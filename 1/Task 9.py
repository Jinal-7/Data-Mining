# TASK 9 COMPLETE

import json
import datetime
import os.path

tweets = []
b = []

for line in open('CrimeReport.txt').readlines():
    tweet = json.loads(line)
    tweets.append(tweet)

for i in range (0, len(tweets)):
    string = tweets[i]['created_at']
    date = datetime.datetime.strptime(string, "%a %b %d %X %z %Y")
    a = date.strftime('%m-%d-%Y %H')
    b.append(a)

#print (b)

path = "/Users/Jinal/PycharmProjects/HW 1 B/Task 9/"

if not os.path.exists(path):
    os.makedirs(path)

for i in range(0, len(b)):
    file_name = b[i] + '.txt'
    with open (os.path.join(path, file_name), 'w') as f:
        c = str(tweets[i])
        f.write(c)