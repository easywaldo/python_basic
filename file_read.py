line = open("data.txt", "r", encoding="utf-8")
for oneLine in line.readlines():
    print(f'line : {oneLine}')

line.close()