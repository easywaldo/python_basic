list = [1, 3, 4, 5, 6, 767, 100]
print(list)
list.sort()
print(list)

for n in list:
    print(n)

list_test = [(1, "waldo"), (2, "ted"), (3, "bob")]

list_test.append((4, "leon"))

list_test.extend([(5, "nix"), (6, "james")])

print(list_test)
