def select_gcd(a, b):
    gcd_value = 0
    min_value = min(a, b)
    for n in range(min_value, 1, -1):
        if a % n == 0 and b % n == 0 and n > gcd_value:
            gcd_value = n
    return gcd_value

print(select_gcd(10, 4))
print(select_gcd(27, 90))



def select_gcd_uqlid(a, b):
    print('select_gcd_uqlid', a, b)
    if b == 0:
        return a
    return select_gcd_uqlid(b, a % b)

print(select_gcd_uqlid(27, 81))
print(select_gcd_uqlid(24, 60))
