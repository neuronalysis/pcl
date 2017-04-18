#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL II, Übung 3, FS17
#Aufgabe 1
#Autor: Christian Fürst
#Matrikel-Nr.: 98-618-192

from collections import Counter
from glob import iglob
import re
import os
import lxml.etree as ET
import operator
from collections import defaultdict



def getfreqwords(indir, outfile):
    d = defaultdict(int)
                
    for filepath in iglob(os.path.join(indir, '*mul.xml')):
        print(filepath)
        tree = ET.parse(filepath)
    
        for article in tree.iterfind('.//article'):
            for sentence in article.iterfind('.//s'):
                words = sentence.iterfind('.//w[@lemma]')
                lemmaSentence = ''
                    
                for index, word in enumerate(words):
                    lemmaSentence += ' ' + word.get('lemma')
                    
                if (index >= 6 and lemmaSentence != ''): d[lemmaSentence] += 1
                    
    with open(outfile, 'w') as outp:
        i=0
        
        for w in sorted(d, key=d.get, reverse=True):
            if(i < 20): 
                outp.write(w + ': ' + str(d[w]))
                outp.write('\n')
                
                i += 1