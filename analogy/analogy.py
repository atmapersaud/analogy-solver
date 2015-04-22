#!/usr/bin/python3

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

def read_model_file_data(filename, data):
    if filename is None:
        return None
    with open(filename, mode='r', errors='ignore', encoding='ISO-8859-1') as file:
        model = defaultdict(list)
        for line in data:
            for word in line:
                model[word] = list()
        for line in file:
            data = line.split()
            if(data[0] in model):
                model[data[0]] = data[1:]
        return model

def solve(model, data):
    for line in data:
        #~ print(line)
        flag = False
        for i in range(len(line)-1):
            if(len(model[line[i]]) == 0):
                print("Out of dictionary word!")
                flag = True
                break
        if(flag):
            continue
        cos = list()
        for i in range(int((len(line)-1)/2)-1):
            cos.append(CalculateCosineSimilarity(model[line[2*(i+1)+1]], model[line[1]]) + CalculateCosineSimilarity(model[line[2*(i+1)+1]], model[line[2*(i+1)]]) - CalculateCosineSimilarity(model[line[2*(i+1)+1]], model[line[0]]))
            #~ print(line[0] + " : " + line[1] + " :: " + line[2*(i+1)] + " : " + line[2*(i+1)+1] + " = " + str(cos[i]))
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
    model = read_model_file_data(args.MODEL, data)
    solve(model, data)


if __name__ == '__main__':
    main()
