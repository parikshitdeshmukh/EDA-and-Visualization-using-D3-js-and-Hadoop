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
stop_words.add("advertisement")
stop_words.add("said")
i=0

def read_input(file):
    for line in file:
        
        yield line.split()

def main(separator='\t'):
    
    data = read_input(sys.stdin)
    print(data)
    is_noun = lambda pos: pos[:2] == 'NN'
    
    for words in data:
        print(words)
        nouns = [word for (word, pos) in nltk.pos_tag(words) if is_noun(pos)]
        print nouns
        words = [noun for noun in nouns if noun not in stop_words]
        print words
       
        for word in words:
            if(not (word.lower() in (stop_words))):
                print '%s%s%d' % (word.lower(),separator, 1)

if __name__ == "__main__":
    main()