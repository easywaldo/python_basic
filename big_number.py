#n, m, k = map(int, input().split())
n = int(input('숫자의 총 갯수를 입력하세요'))
m = int(input('숫자의 총합을 계산할 횟수를 입력하세요'))
k = int(input('특정 요소가 k 번 합산을 초과할 수 없음을 의미하는 수치를 입력하세요'))

#n = 5
#m = 8
#k = 3

#data = list(map(int, input().split(',')))
#data = [2,4,5,4,6]
##data = []
data = list(map(int, input('숫자들을 입력하세요!!!').split()))

data.sort();
##print(data)

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