# # 함수 만들기
# def hello(): # 함수 작성
#     print('하이!')
#     print('안녕!')
#     print('니 하오!')


# hello() # 함수 호출

# 매개변수(파라메타, 인수) 있는 함수
# def hello(name):
#     print('하이 ' + name)


# hello('길동')
# hello('펭수')

# 매개변수 리턴값 있는 함수
# def add10(n):
#     return n + 10


# print(add10(10))

# 예제 1
def is_odd(n):
    if n % 2 == 1:
        print('홀수')
    else:
        print('짝수')


is_odd(1)
is_odd(2)

# 예제 2


def avgNums(*n):  # * : 가변 매개변수(여러개 가능)
    return sum(n)/len(n)


print(avgNums(1, 2, 3))
print(avgNums(1, 2, 3, 4, 5, 6, 7))
