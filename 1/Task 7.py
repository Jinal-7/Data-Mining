# TASK 7 COMPLETE

import json

a = open('CrimeReport.txt').readlines()

for i in range(0, len(a)):
    tweet = json.loads(a[i])
    b = tweet.keys()
    print (tweet['id']) # Gives ID for every tweet

print ('\n')
print (b)