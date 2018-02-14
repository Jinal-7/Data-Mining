import matplotlib.pyplot as plt
import pandas
import numpy

f = open('wine.data')
names = ['Class', 'Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids',
         'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'diluted wines', 'Proline']

data = pandas.read_csv(f, names=names)

correlation = data.corr()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlation, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 14, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()
