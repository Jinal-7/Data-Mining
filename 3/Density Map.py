import matplotlib.pyplot as plt
import pandas

f = open('wine.data')
names = ['Class', 'Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'diluted wines', 'Proline']

data = pandas.read_csv(f, names = names)

data.plot(kind='density', subplots='True', layout=(4, 4), sharex=False)
plt.show()