#!/usr/bin/env python

import quantumrandom
import os
import csv
import sys

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
    args = sys.argv[1:]
    usage = "diceware.py number_of_words [path_to_wordfile]\n"
    if (len(args) != 1) and (len(args) != 2):
        print usage
        exit(1)
    if len(args) > 1:
        if os.path.exists(args[1]):
            worddict = _wordlist_to_dict(args[1])
    else:
        worddict = _wordlist_to_dict(resource_filename(
            Requirement.parse("quantum_diceware"),"quantum_diceware/wordlists/english.asc"))
    numbers = []
    for i in xrange(0, int(args[0])):
        numbers.append(quantumrandom.uint16(ID_LEN))
    lookups = map(lambda x: "".join([str(y) for y in (x % MAX_DIE_VALUE) + 1]), numbers)
    print [worddict[x] for x in lookups]

if __name__ == "__main__":
    main()
