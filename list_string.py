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