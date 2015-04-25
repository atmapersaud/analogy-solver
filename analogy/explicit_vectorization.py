#!/usr/bin/python3
import sys
import json
import math
import argparse
import datetime
import numpy as np
from scipy import sparse
from scipy.sparse import linalg
from sklearn.decomposition import TruncatedSVD

def main():
    infile = open(sys.argv[1])
    outfile = open(sys.argv[2], 'w')
    vocabfile = open(sys.argv[3])
    vocab = json.load(vocabfile)

    F = sparse.dok_matrix((len(vdict), 4*len(vdict)), dtype=np.int32)
    corpus_size = 0
    lc = 0

    for line in infile:
        lc += 1
        if lc % 10000 == 0:
            print('processing line ' + str(lc) + ' at ' + str(datetime.datetime.now()))
        words = line.split()
        num_words = len(words)
        corpus_size += num_words

        if num_words < 5:
            process_short_line(num_words, words, F, vocab)

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
                
    # compute PMI
    Fc = F.tocoo()
    word_freqs = Fc.sum(1)
    context_freqs = Fc.sum(0)

    for i,j,v in zip(Fc.row, Fc.col, Fc.data):
        F[i,j] = max( math.log((v * corpus_size) / (word_freqs[i] * context_freqs[j])), 0 )

    # compute TruncatedSVD
    svd = TruncatedSVD(n_components=200)
    Fred = svd.fit_transform(F)

    np.savetxt(outfile, Fred, delimiter=',')

    infile.close()
    outfile.close()
    vocabfile.close()

def process_short_line(num_words, words, F, vocab):
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
        
if __name__ == '__main__':
    main()
