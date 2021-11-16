import pandas

pd = pandas.read_csv('./text.csv')
print(pd)

import csv

#f = open('text.csv')
with open('text.csv') as fl:
    data = csv.reader(fl, delimiter=',')
    for i in data:
        print(i)
