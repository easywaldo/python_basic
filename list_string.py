from locale import format_string


name: str = "hello world"
print(name.upper())

print(name.replace("world", "세상"))

index = name.find("world")
print(index)
print(name.count("o"))

pipeString = "이름|카테고리|나이|지역"
print(pipeString.split("|"))


print(":".join(['python', 'c#', 'php', 'java', 'react', 'vue']))

print("     hello world ".lstrip())
print(" hello world      ".rstrip())


studentName = "waldo"
duration = 10

message = f"{studentName} 님 수강기간이 {duration} 일 남았습니다"

print(message)


formatString = "{0} 님 수강기간이 {1} 일 남았습니다"
print(formatString.format(studentName, duration))


for index, number in enumerate([1,2,3,4,5,6,76]):
    print(index, number)

list = [1,23,34]
print(list)

list.clear()
print(list)

list.append(77)
print(list)
list.remove(77)
print(list)

numList = [1,2,344,5,567,68,2,3,4,55,7,0]
numList.sort()
print(numList)

del numList[0]
print(numList)


for n in range(10):
    print(n)
result = [x * 2 for x in range(10)]
print(result)
result2 = [x for x in range(10) if x > 5]
print(result2)


listWord = ['apple', 'watch', 'apolo', 'start', 'americano']
searchResult = [n for n in listWord if n.index('a') == 0]
print(searchResult)



listWord = ['오메가3', '비타민C500', None, '홍삼절편', None]
searchResult = [s if s != None else '' for s in listWord]
print(searchResult)