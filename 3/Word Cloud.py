import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud


d = path.dirname(__file__)

text = open(path.join(d, 'Text.txt')).read()
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

