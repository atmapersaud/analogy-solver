#!/usr/bin/python3

def read_csv_file_data(filename):
    if filename is None:
        return None
    with open(filename, mode='r', errors='ignore', encoding='ISO-8859-1') as file:
        import csv
        reader = csv.reader(file, delimiter=',', skipinitialspace=True)
        data = list(reader)
        return data

def generate_formatted_data(data):
    result = list()
    for line in data:
        result.append("{}".format(line[3].lower())) 
        result.append("{}".format(line[5].lower())) 
        result.append("{}".format(line[7].lower())) 
        result.append("{}".format(line[9].lower()))
    return result

def compare(data, predict):
    for i in range(len(data)):
        ans = data[i][10]
        
        pred = list()
        for j in range(4):
            if(predict[4*i+j] and predict[4*i+j][0] != "Out of dictionary word!"):
                pred.append(int(predict[4*i+j][0]) + 1)
            else:
                pred.append(0)
       
        index = pred.index(max(pred))
       
        if(chr(index+64) == ans):
            print(True)
        else:
            print(False)

def main():
    import argparse
    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('FILE1', type=str, help='result')
    parser.add_argument('FILE2', type=str, help='predict')
    args = parser.parse_args()
    
    data = read_csv_file_data(args.FILE1)
    predict = read_csv_file_data(args.FILE2)
    
    compare(data, predict)


if __name__ == '__main__':
    main()
