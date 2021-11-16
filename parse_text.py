import csv

with open('a.txt') as data:
    dt = csv.reader(data,delimiter='!')
    for i in dt:
        print(i)