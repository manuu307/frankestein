# start an NLP proyect with a text file as input and a text file as output
# run the main.py with the input file as argument

import sys
import nltk
import string
# import os
# import re
# import numpy as np
# import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

ntlk.download('stopwords')

# Read the text file and save it as a string
input = sys.argv[1]
text = open(input, 'r', encoding="utf8").read()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Tokenize the text into words
words = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

# Remove words with 2 or less characters
words = [w for w in words if len(w) > 2]

# Remove numbers
words = [w for w in words if not w.isdigit()]

# Remove words that are not alphabetic
words = [w for w in words if w.isalpha()]

# write the output file with the words in the text file as input and the words as output
with open(sys.argv[2], 'w') as f:
    for word in words:
        f.write(word + '\n')
