import nltk
# nltk.download('wordnet')
# nltk.download('vader_lexicon')
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer
text="""Hello i am shivam"""
demowords=['yes','no','shivam']
# lemmatizer=WordNetLemmatizer()
# stemmer=PorterStemmer()
# for word in demowords:
#     print(stemmer.stem(word),lemmatizer.lemmatize(word,'v'))
sia=SentimentIntensityAnalyzer()
# print(sia.polarity_scores('shivam is good'))
print(sia.polarity_scores('shivam is a very bad boy'))

