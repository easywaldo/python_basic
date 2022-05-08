stock_a = {"samsung": 1000, "lg": 2000}
stock_b = {
    "samsung": [1000, 20000, 3000, 5000, 34500],
    "lg": [7000, 20300, 45460]
}
stock_c = {
    "samsung": {
        "current": 1000,
        "stock_count": 30,
        "price": 90100
    }
}

print(stock_a)
print(stock_b)
print(stock_c)

print(stock_c["samsung"]["stock_count"])

# 딕셔너리 할당하기
stock_a["samsung"] = 8000
print(stock_a)

# 딕셔너리 삭제하기
del stock_a["samsung"]
print(stock_a)

stock_d = {
    "samsung": 10000,
    "lg": 2000,
    "naver": 130000,
    "kakao": 90000,
}

print(stock_d.items())
for item in stock_d.items():
    print(item)         # tuple 형태로 접근 가능
    print(item[0])
    print(item[1])

for item in stock_d.keys():
    print(item)

for value in stock_d.values():
    print(value)


# 특정 키 존재하는 지 확인
user = {"name": "사용자", "email": "user@test.com", "age": 25}
print("email" in user)
print("title" in user)

# 사전 병합
dic1 = {"A": 1, "B": 2}
dic2 = {"B": 3, "C": 4}
print({**dic1, **dic2})

# 3.9 이상에서는 | 연산자 이용한 병합이 가능하다
# ßprint(dic1 | dic2)

# 사전 반영
dic1.update(dic2)
print(dic1)

# 3.9 이상에서는 | 연산자 활용하여 반영이 가능하다
dic1 = {"O": 9, "A": 1, "B": 2}
dic2 = {"B": 3, "C": 4}
# dic1 |= dic2
# ßprint(dic1)
