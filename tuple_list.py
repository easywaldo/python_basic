list = list([1,2,3,4,5])

item1, item2, item3, item4, item5 = list

t = tuple(list)

print(list)
print(item1)
print(item2)
print(item3)
print(item4)
print(item5)

print(sum(list))
print(max(list))
print(min(list))
print((min(list), max(list), sum(list)))


print(t)

name, language, age = tuple(["waldo", "python", 42])
print(name)
print(language)
print(age)

t2 = (name, language, age)
print(t2)