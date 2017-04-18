#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL II, Übung 3, FS17
#Aufgabe 1 - TEST
#Autor: Christian Fürst
#Matrikel-Nr.: 98-618-192

from solution_1 import *

def main():
    #for entry in getfreqwords('C:\development\data\SAC_test', 'freq-stats.txt'):
    #    print(entry)
    getfreqwords('C:\development\data\SAC', 'freq-stats.txt')
    
    

if __name__ == '__main__':
    main()