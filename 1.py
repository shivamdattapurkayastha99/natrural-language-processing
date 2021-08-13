import nltk
import matplotlib.pyplot as plt
# nltk.download('punkt')
text="""Hello i am shivam"""
# from nltk.tokenize import word_tokenize
# print(word_tokenize(text))
from nltk.tokenize import word_tokenize
word_tokenized=word_tokenize(text)
# from nltk.tokenize import sent_tokenize
# print(sent_tokenize(text))
from nltk.probability import FreqDist
# print(FreqDist(word_tokenized))
fd=FreqDist(word_tokenized)
print(fd.most_common(3))
fd.plot(30,cumulative=False)
plt.show()

