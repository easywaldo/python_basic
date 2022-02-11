def fun(a,b,c,d,*rest):
    return a,b,c,d,rest

print(fun(*[1,2],3,*range(4,7)))

print(*[1,2])
print(*range(4,7))
print(*range(1,10))
for i in range(4,7):
    print(i)