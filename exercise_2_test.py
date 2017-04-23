#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL II, Übung 4, FS17
#Aufgabe 2 - TEST
#Autor: Christian Fürst
#Matrikel-Nr.: 98-618-192

from solution_2 import *

def main():
    gettitles(
        r'C:\development\data\wiki\dewiki-latest-pages-articles.xml',
        'testfile.txt',
        'trainfile.txt',
        100)
    

if __name__ == '__main__':
    main()