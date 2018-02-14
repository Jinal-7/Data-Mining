import os

tweets = []
for line in open('training_tweets.txt').readlines():
    items = line.split(',')
    tweets.append([int(items[0]), items[1].lower().strip()])

print(len(tweets))
print(tweets[0][0])

a = [item[0] for item in tweets]

path = '/Users/jinal/PycharmProjects/HW 6/Labeled Tweets/'

if not os.path.exists(path):
    os.makedirs(path)

for i in range(len(tweets)):
    if (a[i] == 1):
        file_name = 'Positive Tweets.txt'
        with open(os.path.join(path, file_name), 'a') as f:
            c = str(tweets[i])
            f.write(c)

    elif (a[i] == 0):
        file_name = 'Negative Tweets.txt'
        with open(os.path.join(path, file_name), 'a') as f:
            c = str(tweets[i])
            f.write(c)

    else:
        file_name = 'Unlabeled Tweets.txt'
        with open(os.path.join(path, file_name), 'a') as f:
            c = str(tweets[i])
            f.write(c)

