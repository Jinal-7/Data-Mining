import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import re

type = []
legs = []
temp = ""

for line in open('zoo.data').readlines():
    temp = line
    a = re.findall('\d+', temp)
    type.append(int(a[16]))
    legs.append(int(a[12]))

x = type
y = legs
plt.title("Types of Animals have how many Legs")

plt.plot(x, y, 'o')
plt.ylabel("Legs")
plt.xlabel("Type")

plt.show()