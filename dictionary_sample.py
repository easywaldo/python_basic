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


## 딕셔너리 할당하기
stock_a["samsung"] = 8000
print(stock_a)

## 딕셔너리 삭제하기
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
    print(item) ## tuple 형태로 접근 가능
    print(item[0])
    print(item[1])

for item in stock_d.keys():
    print(item)
    
for value in stock_d.values():
    print(value)