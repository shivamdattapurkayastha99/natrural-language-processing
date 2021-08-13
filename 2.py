import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
text="""Hello i am shivam"""
demowords=['yes','no','shivam']
# print(stop_words)
from nltk.tokenize import word_tokenize,sent_tokenize
tokenize_words=word_tokenize(text)
# print(tokenize_words)
tokenize_words_without_stop_words=[]
for word in tokenize_words:
    if word not in stop_words:
        tokenize_words_without_stop_words.append(word)
print(set(tokenize_words)-set(tokenize_words_without_stop_words))
print(tokenize_words)
print(tokenize_words_without_stop_words)







