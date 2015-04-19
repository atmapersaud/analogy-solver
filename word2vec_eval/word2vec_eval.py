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

def compare(result, predict):
    for i in range(len(result)):
        print(result[i], end=", ")
        if(predict[i][0] == "Out of dictionary word!"):
            print("Out of dictionary word!")
            continue            
        flag = True        
        for j in range(100):
            if(result[i] == predict[i][j*2]):
                print("{}, {}".format(j, predict[i][j*2+1]))
                flag = False
                break                
        if(flag):
            print()

def main():
    import argparse
    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('FILE1', type=str, help='result')
    parser.add_argument('FILE2', type=str, help='predict')
    args = parser.parse_args()
    
    data = read_csv_file_data(args.FILE1)
    result = generate_formatted_data(data)
    
    predict = read_csv_file_data(args.FILE2)
    
    compare(result, predict)


if __name__ == '__main__':
    main()
