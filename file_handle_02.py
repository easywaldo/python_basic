file = open("data.txt", "a", encoding="utf-8")
file.write("\nhello world")
file.close()


read = open("data.txt", "r", encoding="utf-8")
data = read.read()
print(data)
read.close()