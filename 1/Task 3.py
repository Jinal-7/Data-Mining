# TASK 3 COMPLETE

# Write a File
f = open("task3.data", "w")

for i in range(10):
    f.write("%d\t" %(i+1))

f.close()

item1 = []
item2 = []

# Function to read the File
def f_read():
    f = open("task3.data", "r")
    f.read()
    f.close()

for i in range(0,5):
    item1.append(i+1)

for i in range(5,10):
    item2.append(i+1)

print (item1)
print (item2)

f_read()