import csv

data = [
    ['name', 'age', 'department'],
    ['john', '22', 'computer'],
    ['waldo', '33', 'science'],
]

file = open('sample.csv', 'w', newline="", encoding='utf-8-sig')
writer = csv.writer(file)

for row in data:
    writer.writerow(row)

file.close()