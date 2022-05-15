s = 'I am ' + str(7) + ' years old'
print(s)

friends = [('Jung', 22), ('Hone', 23), ('Park', 24)]
for f in friends:
    print('My friend', f[0], 'is', f[1], 'years old')
    s = 'My friend ' + f[0] + ' is ' + str(f[1]) + ' years old'
    print(s)

s = 'My name is %s ' % 'Waldo'
print(s)


# String format using tuple
s = 'My friend %s is %d years old and %fcm tall. ' % ('Jung', 22, 178.5)
print(s)

# String format using tuple in loop
for f in friends:
    print('My friend %s is %d years old' % (f[0], f[1]))

print('%f' % 101)

print('%d' % 3.14)


# String format using dictionary
s = '%(name)s : %(age)d ' % {'name': 'easywadlo', 'age': 42}
print(s)


# String format width
print('height: %f' % 3.14)
print('height: %.3f' % 3.14)
print('height: %.2f' % 3.14)

print('height: %7.2f입니다.' % 3.14)
print('height: %10.2f입니다.' % 3.14)

print('height: %07.2f입니다.' % 3.14)
print('height: %010.2f입니다.' % 3.14)
