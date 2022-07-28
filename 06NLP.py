# Sentence Tokenization 
import nltk
nltk.download('punkt')


from nltk.tokenize import sent_tokenize
text = "Hello everyone. Welcome to GeeksforGeeks. You are studying NLP article"
sent_tokenize(text)

# Word Tokenization – Splitting words in a sentence.
from nltk.tokenize import word_tokenize
  
text = "Hello everyone. Welcome to GeeksforGeeks."
word_tokenize(text)