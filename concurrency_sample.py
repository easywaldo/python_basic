# 병행성
# 이터레이터, 제너레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, uppacking, *args...: iterable

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(dir(t))

for c in t:
    pass
    # print(c)

# while
w = iter(t)

print(dir(w))
print(next(w))

print(next(w))
print(next(w))
print(next(w))

# while
while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()


# 반복형 확인
print(hasattr(t, '__iter__'))

from collections import abc

print(isinstance(t, abc.Iterable))
print()


# next 패턴
class WordSplitter:
    def __init__(self, text):
        self.idx = 0
        self.text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self.text[self.idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self.idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self.text)


wr = WordSplitter('Do today what you could do tomorrow')
# print(wr)
# print(next(wr))
# print(next(wr))
# print(next(wr))
# print(next(wr))
# print(next(wr))
# print(next(wr))
# print(next(wr))
# print(next(wr))
# print(next(wr))


print()
print()



# generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 => 데이터 양 증가 후 메모리 사용량 증가 >> 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각 사용량

class WordSplitGenerator:
    def __init__(self, text):
        self.text = text.split(' ')
    
    def __iter__(self):
        for word in self.text:
            yield word # << 제너레이터
        return 

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self.text)
    
wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg)

print(wt)
print(wg)

print()

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
