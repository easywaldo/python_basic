##n, m, k = map(int, input().split())
n = 5
m = 8
k = 3
#data = list(map(int, input().split()))
data = [2,4,5,4,6]

data.sort();
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if (m == 0):
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)