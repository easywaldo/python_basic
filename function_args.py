# 위치가변 매개변수 함수
def print_fruits(*args):
    print(args)
    for arg in args:
        print(arg)


print_fruits('apple', 'orange', 'mango', 'grape')


# 키워드가변 매개변수 함수
def comment_info(**kwargs):
    print(kwargs)
    for arg in kwargs:
        print(arg)

    for key, value in kwargs.items():
        print(f'key:{key} value:{value}')


comment_info(name='python', content='FastAPI')


# 매개변수 작성 순서 (1. 위치 , 2. 위치가변, 3. 키워드, 4. 키워드가변)
def post_info(title, content, *tags):
    print('post_info')
    print(f'제목:{title}, 내용:{content}, 태그{tags}')


def post_info_v2(*tags, title, content, **kwargs):
    print('post_info')
    print(f'제목:{title}, 내용:{content}, 태그{tags}, 키워드{kwargs}')


post_info('파이썬 프로그래밍', '합수의 다양한 실습', '#파이썬', '#FastAPI')
post_info_v2('#파이썬', '#FastAPI', title='파이썬 프로그래밍', content='합수의 다양한 실습')
post_info_v2(
    '#파이썬', 
    '#FastAPI', 
    title='파이썬 프로그래밍', 
    content='합수의 다양한 실습', 
    lectureName='redis', 
    lectureDescription='cache server')