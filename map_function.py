def strip_all(x):
    return x.strip()


items = [' 로지텍 마우스 ', ' 키보드 ']
print(items)
items = list(map(strip_all, items))

print(items)


result = list(map(lambda x: x.strip(), [' 브라보콘 ', '구구 크러스터 ']))
print(result)