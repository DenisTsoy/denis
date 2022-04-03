from sys import argv
from itertools import islice
f1_name='./bakery.csv'

with open(f1_name , 'r', encoding='utf-8') as f:
    if len(argv) == 1:
        content = f.read()
        print(content)
    elif len(argv) == 2:
        for line in islice(f, 0, int(argv[1])):
            print(line.rstrip())
    elif len(argv) == 3:
        for line in islice(f, (int(argv[1])-1), int(argv[2])):
            print(line.rstrip())





