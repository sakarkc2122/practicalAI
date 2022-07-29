import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize
text = "My name is Sakar KC. I am awesome."
list1 = sent_tokenize(text) # Sentence Tokenization
print(list1)

from nltk.tokenize import word_tokenize
  
text = "My name is Sakar"
list2 = word_tokenize(text) # Word Tokenization
print(list2)