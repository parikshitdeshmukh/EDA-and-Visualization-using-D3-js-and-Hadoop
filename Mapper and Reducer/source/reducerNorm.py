#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""


## Parikshit Sunil Deshmukh - pdeshmuk -  50247649
## Mahalakshmi Padma Sri Harsha Maddu - mmaddu - 50246769

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    
    data = read_mapper_output(sys.stdin, separator=separator)
    d={}

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            d[str(current_word).strip()]=total_count
           
        except ValueError:
            
            pass
    keys = sorted(d, key=d.get, reverse=True)
    i=0
    print "%s%s%s" % ("text",separator, "size".strip())
    for x in keys:
        print "%s%s%d" % (x.strip(),separator, d[x])
        i=i+1
        if i==100:
            break;

if __name__ == "__main__":
    main()