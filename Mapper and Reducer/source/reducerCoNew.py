#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""



## Parikshit Sunil Deshmukh - pdeshmuk -  50247649
## Mahalakshmi Padma Sri Harsha Maddu - mmaddu - 50246769

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 2)

def main(separator='\t'):
    
    data = read_mapper_output(sys.stdin, separator=separator)
    data1=data
    
    d={}
    top=[]
    coDict={}
    temp=[]
   
    j=0
    for current_word, group in groupby(data, itemgetter(0)):
        temp=[]
        total_count=0
        try:
            
            try:
                for c, z, y in group:
                    total_count=total_count+int(z)
                    
                    temp.append(y)
            except ValueError:
                pass
            
            d[current_word]=[total_count, temp]
            
        except ValueError:
            
            pass

    keys = sorted(d, key=d.get, reverse=True)
    i=0
    print "Below Output gives a list of Co-occurring word with top 10 words."
    print "%s%s%s" % ("text", ",", "size,  Co-occurances")
    for x in keys:
        du= set(d[x][1])
        print "%s%s%d\t%s\n" % (x, ",   ", d[x][0], du)
        top.append(x)
        i=i+1
        if i==10:
            break;



if __name__ == "__main__":
    main()