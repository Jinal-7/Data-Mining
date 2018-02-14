# TASK 5 COMPLETE

import json

data1 = {"School": "UAlbany", "Address": "1400 Washington Ave, Albany, NY 12222", "Phone": "(518) 442-3300"}

a = json.dumps(data1, indent= 3)
print (a)

b = json.loads(a)
print (b) # Print Items

print (b.keys()) # Print Keys
print (b.values()) # Print Value

data2 = '{"Major": "Computer Science", "Year": "Spring 2017", "Subject": "Data Mining"}'

c = json.loads(data2)
print (c) # Print Items

print (c.keys()) # Print Keys
print (c.values()) # Print Values