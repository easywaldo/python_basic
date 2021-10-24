n = int(input('세로의 길이를 입력해주세요\n'))
m = int(input('가로의 길이를 입력해주세요\n'))

data = list(map(int, input('숫자들을 입력해주세요.').split()))

result = 0

# for i in range(n):
#     data = list(map(int, input().split()))
#     print(data)
#     min_value = min(data)
#     result = max(result, min_value)

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 99999
    for lineNumber in data:
        min_value = min(min_value, lineNumber)
    result = max(result, min_value)

print(result)
