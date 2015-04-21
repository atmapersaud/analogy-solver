#!/usr/bin/python3

import sys
import argparse
import numpy as np
from scipy import sparse

def main():
    infile = open(sys.argv[1])
    outfile = open(sys.argv[2], 'w')
    vocabfile = open(sys.argv[3])
    vdict = json.load(vocabfile)

    F = sparse.lil_matrix((len(vdict), 4*len(vdict)))
    for line in infile:
        words = line.split()
        num_words = len(words)

        if num_words < 2:
            continue

        elif num_words == 2:
            F[vocab[words[0]], 4 * vocab[words[1]] + 2] += 1

            F[vocab[words[1]], 4 * vocab[words[0]] + 1] += 1

        elif num_words == 3:
            F[vocab[words[0]], 4 * vocab[words[1]] + 2] += 1
            F[vocab[words[0]], 4 * vocab[words[2]] + 3] += 1

            F[vocab[words[1]], 4 * vocab[words[0]] + 1] += 1
            F[vocab[words[1]], 4 * vocab[words[2]] + 2] += 1

            F[vocab[words[2]], 4 * vocab[words[0]] + 0] += 1
            F[vocab[words[2]], 4 * vocab[words[1]] + 1] += 1

        else:
            F[vocab[words[0]], 4 * vocab[words[1]] + 2] += 1
            F[vocab[words[0]], 4 * vocab[words[2]] + 3] += 1

            F[vocab[words[1]], 4 * vocab[words[0]] + 1] += 1
            F[vocab[words[1]], 4 * vocab[words[2]] + 2] += 1
            F[vocab[words[1]], 4 * vocab[words[3]] + 3] += 1

            F[vocab[words[-2]], 4 * vocab[words[-4]] + 0] += 1
            F[vocab[words[-2]], 4 * vocab[words[-3]] + 1] += 1
            F[vocab[words[-2]], 4 * vocab[words[-1]] + 2] += 1

            F[vocab[words[-1]], 4 * vocab[words[-3]] + 0] += 1
            F[vocab[words[-1]], 4 * vocab[words[-2]] + 1] += 1
            
            for i, word in enumerate(words[2:-2]):
                F[vocab[word], 4 * vocab[words[i-2]] + 0] += 1
                F[vocab[word], 4 * vocab[words[i-1]] + 1] += 1
                F[vocab[word], 4 * vocab[words[i+1]] + 2] += 1
                F[vocab[word], 4 * vocab[words[i+2]] + 3] += 1
                
    # convert to sparse mat representation
    # put a pause here to check memory
    Fsr = F.tocsr()
    Fsc = F.tocsc()
    # compute PMI
    # compute SVD

    infile.close()
    outfile.close()
    vocabfile.close()

if __name__ == '__main__':
    main()
