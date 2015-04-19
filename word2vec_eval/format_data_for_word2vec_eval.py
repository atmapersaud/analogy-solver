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
    for line in data:
        print("{} {} {}".format(line[0].lower(), line[1].lower(), line[2].lower())) 
        print("{} {} {}".format(line[0].lower(), line[1].lower(), line[4].lower())) 
        print("{} {} {}".format(line[0].lower(), line[1].lower(), line[6].lower())) 
        print("{} {} {}".format(line[0].lower(), line[1].lower(), line[8].lower()))
    print("EXIT")

def main():
    import argparse
    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('FILE', type=str, help='filename')
    args = parser.parse_args()
    
    data = read_csv_file_data(args.FILE)
    generate_formatted_data(data)


if __name__ == '__main__':
    main()
