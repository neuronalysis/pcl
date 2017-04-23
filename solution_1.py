#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL II, Übung 3, FS17
#Aufgabe 1
#Autor: Christian Fürst
#Matrikel-Nr.: 98-618-192

from collections import defaultdict
from glob import iglob
import os
import lxml.etree as ET

def getfreqwords(indir, outfile):
    d = defaultdict(int)
                
    with open('hash-sentence-map.txt', 'w', encoding='utf-8') as hashmap:
        for filepath in iglob(os.path.join(indir, '*mul.xml')):
            print(filepath)
            tree = ET.parse(filepath)
        
            for article in tree.iterfind('.//article'):
                for sentence in article.iterfind('.//s'):
                    words = sentence.iterfind('.//w[@lemma]')
                    lemmaSentence = ''
                        
                    for index, word in enumerate(words):
                        lemmaSentence += ' ' + word.get('lemma')
                        
                    if (index >= 6 and lemmaSentence != ''): 
                        d[hash(lemmaSentence)] += 1
                        
                        hashmap.write(
                            str(hash(lemmaSentence)) + '\t' + lemmaSentence
                            )
                        hashmap.write('\n')
    
    top20 = get_top_20_frequencies(d)
        
    processed = defaultdict(int)
    with open('hash-sentence-map.txt') as inp, \
            open(outfile, 'w') as outp:

        mapped_hashes = iter_mapped_hashes(inp)

        for hashmap_entry in mapped_hashes:
            if(top20[hashmap_entry[0]] and not(processed[hashmap_entry[0]])):
                outp.write(
                    hashmap_entry[1] + ': ' + str(top20[hashmap_entry[0]])
                    )
                outp.write("\n")
                
                processed[hashmap_entry[0]] = 1

def iter_mapped_hashes(stream):
    for line in stream:
        yield line.rstrip().split("\t")

def get_top_20_frequencies(unordered_dict):
    i=0
    
    top20 = defaultdict(int)
    
    for w in sorted(unordered_dict, key=unordered_dict.get, reverse=True):
        if(i < 20): 
            top20[str(w)] = unordered_dict[w]
            
            i += 1

    return top20