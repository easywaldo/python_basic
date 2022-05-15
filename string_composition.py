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
