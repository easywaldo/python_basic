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

# String format width right side
print('height: %-7.2f입니다.' % 3.14)
print('height: %-10.2f입니다.' % 3.14)


# String format number flag
n = 3
print('num: %+d' % n)

n = -8
print('num: %+d' % n)


# String format dictionary flag
print('height: %-+10.3f입니다.' % 3.14)

print('%(h)s: %(v)-+10.3f입니다.' % {'h': 'height', 'v': 3.143435})


# string format method
fs = '{0}...{1}...{2}'
ms = fs.format('Robot', 124, 'Box')
print(ms)

print('{0}...{1}...{2}'.format('waldo', '124', 'Box'))
