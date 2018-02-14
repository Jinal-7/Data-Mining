import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import re

type = []
legs = []
temp = ""

for line in open('zoo.data').readlines():
    temp = line
    a = re.findall('\d+', temp)
    type.append(int(a[16]))
    legs.append(int(a[12]))

type.sort()
legs.sort()

data = [type, legs]

plt.title('Type and Legs Box Plot')
plt.boxplot(data)

plt.show()
