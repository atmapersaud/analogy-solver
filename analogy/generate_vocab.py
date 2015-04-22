#!/usr/bin/python3

import sys
import json

def main():
    infile = open(sys.argv[1])
    outfile = open(sys.argv[2], 'w')

    vocab = frozenset(word for line in infile for word in line.split())
    vdict = {word:i for i, word in enumerate(sorted(vocab))}
    json.dump(vdict, outfile)

if __name__ == '__main__':
    main()
