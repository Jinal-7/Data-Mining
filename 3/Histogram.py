import numpy as np
import matplotlib.pylab as plt
import re

type = []
temp = ""

for line in open('zoo.data').readlines():
    temp = line
    a = re.findall('\d+', temp)
    type.append(int(a[16]))

print(type)

bins = [0, 1, 2, 3, 4, 5, 6, 7]
plt.hist(type, bins)
plt.title("Types of Animals")
plt.ylabel("Value")
plt.xlabel("Type")
plt.show()
