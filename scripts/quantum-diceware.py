#!/usr/bin/env python

import quantumrandom
import os
import csv
import sys
import argparse
import logging

from pkg_resources import Requirement, resource_filename

ID_LEN = 5
MAX_DIE_VALUE = 6

def _wordlist_to_dict(wordfile):
    with open(wordfile) as in_handle:
        d = {}
        for line in csv.reader(in_handle, delimiter="\t", quotechar='\''):
            d[line[0]] = line[1]
        return d

def main():
    parser = argparse.ArgumentParser(description="Generates passphrases.")

    parser.add_argument("numwords", 
                            help="The number of words to generate")
    parser.add_argument("-s", "--separator", 
                            help="The separator to use between words")
    parser.add_argument("-f", "--wordfile",
                            help="Filesystem path to a dictionary")

    args = parser.parse_args()

    if(args.wordfile != None):
        worddict = _wordlist_to_dict(args.wordfile)
    else:
        worddict = _wordlist_to_dict(resource_filename(
        Requirement.parse("quantum_diceware"),
            "quantum_diceware/wordlists/english.asc"))

    numbers = []

    for i in xrange(0, int(args.numwords)):
        numbers.append(quantumrandom.uint16(ID_LEN))
    lookups = map(lambda x: "".join([str(y) for y in (x % MAX_DIE_VALUE) + 1]), numbers)

    if(args.separator != None):
        first = None
        for x in lookups:
            if first == None:
                first = worddict[x]
            else:
                sys.stdout.write(worddict[x]) 
                sys.stdout.write(args.separator)
            
        sys.stdout.write(first + "\n")
    else:
        print [worddict[x] for x in lookups]

if __name__ == "__main__":
    main()
