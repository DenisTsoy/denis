def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

import sys

sales = sys.argv[1]
f1_name='./bakery.csv'

if is_number(sales.replace(',','.')):
    with open(f1_name, 'a', encoding='utf-8') as f1:
        print(sales, file=f1)
