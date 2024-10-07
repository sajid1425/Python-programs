#Sentence & Words Tokenization

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
text = "This is smaple sentence and my name Alfaj.       This is sample sentence 2"
words=word_tokenize(text)
print(words)
sentence=sent_tokenize(text)
print(sentence)