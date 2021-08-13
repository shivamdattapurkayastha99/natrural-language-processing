import nltk
from nltk.corpus import wordnet
# syn=wordnet.synsets('computer')
# print(syn[0].definition())
synonyms=[]
for syn in wordnet.synsets('computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)
