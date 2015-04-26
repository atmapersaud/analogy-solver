#!/usr/bin/python3

import sys
import itertools
from collections import defaultdict

def CalculateCosineSimilarity(vecA, vecB):
    dotProduct = DotProduct(vecA, vecB)
    magnitudeOfA = Magnitude(vecA)
    magnitudeOfB = Magnitude(vecB)
    return dotProduct/(magnitudeOfA*magnitudeOfB)

def DotProduct(vecA, vecB):
    dotProduct = 0;
    for i in range(len(vecA)):
        dotProduct += (float(vecA[i]) * float(vecB[i]))
    return dotProduct

def Magnitude(vector):
    import math
    return math.sqrt(DotProduct(vector, vector))

def read_csv_file_data(filename):
    if filename is None:
        return None
    with open(filename, mode='r', errors='ignore', encoding='ISO-8859-1') as file:
        import csv
        reader = reader = csv.reader(file, delimiter=',', skipinitialspace=True)
        data = list(reader)

        result = list()
        for row in data:
            result.append([r.lower() for r in row])
        return result

def read_file_data(filename, data):
    if filename is None:
        return None

    postag = defaultdict(set)
    model = defaultdict(list)

    with open(filename, mode='r', errors='ignore', encoding='ISO-8859-1') as file:
        for line in data:
            for word in line:
                postag[word] = set()
        for line in file:
            word = line.split()[0].split('_')
            if len(word) < 2:
                continue
            if(word[0] in postag):
                postag[word[0]].add(word[1])
                
    with open(filename, mode='r', errors='ignore', encoding='ISO-8859-1') as file:
        for word in postag:
            for tag in postag[word]:
                var = word + "_" + tag
                model[var] = list()
        for line in file:
            var = line.split()
            if(var[0] in model):
                model[var[0]] = var[1:]
                
        return postag, model

def solve(model, postag, data):
    for line in data:
        #~ print(line)
        cos = list()
        
        flag = False
        for i in range(len(line)-1):
            if(len(postag[line[i]]) == 0):
                print("Out of dictionary word!")
                flag = True
                break
        if(flag):
            continue
        
        for i in range(int((len(line)-1)/2)-1):
            cos1 = list()
            temp = list()

            var1 = list()
            var1.append(list(postag[line[0]]))
            var1.append(list(postag[line[1]]))
            var1.append(list(postag[line[2*(i+1)]]))
            var1.append(list(postag[line[2*(i+1)+1]]))
            var2 = list(itertools.product(*var1))
            for tag in var2:
                temp.append(line[0]+"_"+tag[0] + " : " + line[1]+"_"+tag[1] + " :: " + line[2*(i+1)]+"_"+tag[2] + " : " + line[2*(i+1)+1]+"_"+tag[3])
                cos1.append(CalculateCosineSimilarity(model[line[2*(i+1)+1]+"_"+tag[3]], model[line[1]+"_"+tag[1]]) + CalculateCosineSimilarity(model[line[2*(i+1)+1]+"_"+tag[3]], model[line[2*(i+1)]+"_"+tag[2]]) - CalculateCosineSimilarity(model[line[2*(i+1)+1]+"_"+tag[3]], model[line[0]+"_"+tag[0]]))
        
            index = cos1.index(max(cos1))
            cos.append(cos1[index])
            #~ print(temp[index] + " = " + str(cos1[index]))           

        index = cos.index(max(cos))
        #~ print(cos[index])
        if(chr(index+97) == line[-1]):
            print(True)
        else:
            print(False)

def main():
    import argparse
    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('MODEL', type=str, help='model')
    parser.add_argument('FILE', type=str, help='filename')
    args = parser.parse_args()

    data = read_csv_file_data(args.FILE)
    postag, model = read_file_data(args.MODEL, data)

    solve(model, postag, data)


if __name__ == '__main__':
    main()
