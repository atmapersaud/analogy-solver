#!/usr/bin/python3

# usage: ./answer.py word-a word-a* word-b

import sys
import argparse
import subprocess
import dbpedia_module

def main():
    dfile = open('/usr/share/dict/words')
    english = {line.strip() for line in dfile}

    results = []

    a = sys.argv[1]
    astar = sys.argv[2]
    b = sys.argv[3]
    if astar.startswith(a):
        suffix = astar[len(a):]
        if len(suffix) < 4:            
            bstar = b + suffix
            #print(' '.join([a,astar,b,bstar]))
            if bstar in english:
                results.append(bstar)
    elif astar.endswith(a):
        prefix = astar[:len(astar)-len(a)]
        if len(prefix) < 4:
            bstar = prefix + b
            #print(' '.join([a,astar,b,bstar]))
            if bstar in english:
                results.append(bstar)

    results.append(dbpedia_module.answer_query(a, astar, b))
    results.append(subprocess.check_output(['lib/modified-word-analogy', 'vectors.bin ' + a + ' ' + astar + ' ' + b], universal_newlines=True))
    print('\n'.join(results))
    
if __name__ == '__main__':
    main()
