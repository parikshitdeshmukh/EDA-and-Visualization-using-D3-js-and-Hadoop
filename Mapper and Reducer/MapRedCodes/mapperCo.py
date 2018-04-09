#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

## Parikshit Sunil Deshmukh - pdeshmuk -  50247649
## Mahalakshmi Padma Sri Harsha Maddu - mmaddu - 50246769


import sys
import io
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
stop_words.add("said")

i=0

def read_input(file):
    for line in file:
        
        yield line.split()

def main(separator='\t'):
    
    data = read_input(sys.stdin)
    top_words=["tesla","model","company","musk","autopilot","car","system","crash","production","driver"]
    
    is_noun = lambda pos: pos[:2] == 'NN'

    for words in data:
        
        nouns = [word for (word, pos) in nltk.pos_tag(words) if is_noun(pos)]
        

        i=0
        for word in words:
            if i != (len(words) - 1):
                if word in top_words and words[i+1] in nouns and words[i+1] not in stop_words:
                        print '%s\t%s' % (word.lower() + " " + words[i + 1].lower(), 1)
                i = i + 1

if __name__ == "__main__":
    main()