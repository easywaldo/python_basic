import csv

file = open('sample.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(file)

for row in reader:
    print(row)
    
file.close()
