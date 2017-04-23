#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL II, Übung 3, FS17
#Aufgabe 1
#Autor: Christian Fürst
#Matrikel-Nr.: 98-618-192
from lxml import etree as et
import random


def gettitles(infile, testfile, trainfile, k):
    context = et.iterparse(
        infile, 
        tag='{http://www.mediawiki.org/xml/export-0.10/}title', 
        events = ('end', )
        )
    
    my_randoms = random.sample(range(10000), k)
    
    with open(testfile, 'wb') as outTest, \
                    open(trainfile, 'wb') as outTrain:
        
        index = 0
        for event, elem in context:
            if (index in my_randoms):
                outTest.write(bytes(elem.text + "\n", 'UTF-8'))
            else:
                outTrain.write(bytes(elem.text + "\n", 'UTF-8'))
                
            index += 1
            
            elem.clear()
            
            for ancestor in elem.xpath('ancestor-or-self::*'):
                while ancestor.getprevious() is not None:
                    del ancestor.getparent()[0]