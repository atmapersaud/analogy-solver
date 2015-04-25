#!/usr/bin/python3

import sys

def main():
    for line in sys.stdin:
        words = line.split()
        if len(words) > 5:
            print(' '.join(words))

if __name__ == '__main__':
    main()

