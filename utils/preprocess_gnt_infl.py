#!/usr/bin/env python
'''
Generates GloVe training data from GNT corpus with inflections
'''

# This script needs to be run from the home directory
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '.'))

import csv
import unicodedata
import codecs
import fnmatch
import string

from os import path

datapath = 'data/gnt/'
outfile = 'data/gnt/corpus_infl'


def create_txt(datapath, outfile):
    for root, dirs, files in os.walk(datapath):
        for name in fnmatch.filter(files, '*.txt'):
            infile = os.path.join(root, name)
            print(infile)
            with codecs.open(infile, "r", "utf-8") as fin:
                with codecs.open(outfile, "a+", "utf-8") as fout:
                    for line in fin:
                        linesplit = line.split(' ')
                        tok = linesplit[5].strip().translate(str.maketrans('', '', string.punctuation))
                        fout.write(tok + ' ')
                    fout.write('\n')


if __name__ == "__main__":
    create_txt(datapath, outfile)