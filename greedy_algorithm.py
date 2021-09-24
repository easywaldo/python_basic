n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    temp_count = n / coin
    ##print (temp_count)
    n -= coin * temp_count
    count += temp_count

print(count)