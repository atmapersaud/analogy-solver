#!/usr/bin/python3

# usage: ./answer.py word-a word-a* word-b

import sys
import argparse
import dbpedia_module

def main():
    dfile = open('/usr/share/dict/words')
    english = {line.strip() for line in dfile}

    a = sys.argv[1]
    astar = sys.argv[2]
    b = sys.argv[3]
    if astar.startswith(a):
        suffix = astar[len(a):]
        if len(suffix) < 4:            
            bstar = b + suffix
            #print(' '.join([a,astar,b,bstar]))
            if bstar in english:
                print(bstar)
                return
    elif astar.endswith(a):
        prefix = astar[:len(astar)-len(a)]
        if len(prefix) < 4:
            bstar = prefix + b
            #print(' '.join([a,astar,b,bstar]))            
            if bstar in english:
                print(bstar)
                return

    dbpedia_results = dbpedia_module.answer_query(a, astar, b)
    if len(dbpedia_results) > 0:
        print(dbpedia_results[0])
    else:
        result = subprocess.check_output(['lib/modified-word-analogy', 'vectors.bin ' + a + ' ' + astar + ' ' + b], universal_newlines=True)
        print(result.split('\n')[2]) # the first two lines of the response are a header to be skipped

if __name__ == '__main__':
    main()
