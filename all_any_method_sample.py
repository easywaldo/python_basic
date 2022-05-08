def positive_even(num):
    print(f"positive_even({num})")
    return num > 0 and num % 2 == 0


print(all(x % 2 == 0 for x in [2, 4, 6, 8, 10, 12]))

print(all(x % 2 == 0 for x in [1, 3, 5, 6, 8, 10, 12]))

print(all(positive_even(x) for x in [2, 4, 6, 8, 10, 12]))

print(any(positive_even(x) for x in [2, 3, 6, 9, 10, 12]))
