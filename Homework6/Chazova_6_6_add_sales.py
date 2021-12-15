import sys

with open('Bakery.csv', 'a', encoding="utf-8") as f:
    f.write(sys.argv[1]+'\n')