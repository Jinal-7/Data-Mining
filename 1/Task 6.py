# TASK 6 COMPLETE

import json

data = {"School": "UAlbany", "Address": "1400 Washington Ave, Albany, NY 12222", "Phone": "(518) 442-3300"}

items = [1, 2, 3, 4, 5]

#Method 1

with open('task6.data', 'w') as file1:
    json.dump(items, file1)

with open('task6.data') as file1:
    data1 = json.load(file1)
    print (data1)

with open('task6.data', 'w') as file1:
    json.dump(data, file1)

with open('task6.data') as file1:
    data2 = json.load(file1)
    print (data2)

with open('task6.data', 'a') as file1:
    json.dump(items, file1)

'''
# Method 2

with open('task6.data', 'w') as file:
    json.dump(items, file)
    json.dump(data, file)

a = open('task6.data').readlines()
print (a)
'''