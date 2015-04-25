#!/usr/bin/python3

import sys
import json

def main():
    vocab = frozenset(word for line in sys.stdin for word in line.split())
    vdict = {word:i for i, word in enumerate(sorted(vocab))}
    #print(len(vdict))
    print(json.dumps(vdict))

if __name__ == '__main__':
    main()
