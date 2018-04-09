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
#import StringIO

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stop_words.add("said")

i=0

def read_input(file):
    for line in file:
        
        yield line.split()

def main(separator='\t'):
    
    data = read_input(sys.stdin)
    for words in data:
       
        i=0
        for word in words:
            if i!=(len(words)-1):
                if(not (word.lower() in stop_words) and not (words[i + 1].lower() in stop_words)):
                    print '%s\t%s' % (word.lower() + " " + words[i + 1].lower(), 1)
            i = i + 1

if __name__ == "__main__":
    main()