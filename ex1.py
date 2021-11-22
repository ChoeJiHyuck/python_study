# 연습문제
# 01. 두 수의 곱을 리턴하는 함수
import time             # 시간 라이브러리
# import RPi.GPIO as GPIO  # 라즈베리파이 GPI0사용 모듈


def mult_two(a, b):
    # 함수를 완성시킨다.
    return a*b


if __name__ == '__main__':
    print(mult_two(3, 2))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0

# 02. 튜플 (3개 입력 이상) 을 입력받아서
# 첫번째 값, 세번째 값, 끝에서 두번째 값을 튜플로 만들어 리턴


def easy_unpack(elements):
    return (elements[0], elements[2], elements[-2])  # 튜플로 리턴


if __name__ == '__main__':
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)

# 03. 한 단어만 끊어서 리턴한다.
# 만약 끊어진 단어가 없다면 단어 전체 리턴


def first_word(text):
    return text.split()[0]


if __name__ == '__main__':
    print(first_word("Hello world"))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"

# 04. 패스워드는 길이가 6보다 커야 한다. => 크면 True 틀리면 False 리턴


def is_acceptable_password(password):
    return len(password) > 6


if __name__ == '__main__':
    print(is_acceptable_password('short'))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False

# 05. 정수(int)의 길이를 구하라.


def number_length(a):
    return len(str(a))


if __name__ == '__main__':
    print(number_length(10))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2

# 06. 문자열을 입력 받아서 역순으로 리턴


def backward_string(val):
    return val[::-1]


if __name__ == '__main__':
    print(backward_string('val'))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'

# 07. 리스트 items 와 정수 i를 입력받아,
# 만약 i가 items에 있으면 i 앞의 숫자들을 제거하고 리턴
# Alt text


def remove_all_before(items, i):

    if i in items:
        # 코드 작성
        return items[items.index(i):]
    else:
        return items


if __name__ == '__main__':
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [
        7, 7, 7, 7, 7, 7, 7, 7, 7]

# 08. text 문자열을 입력받아 문자열의 문자가
# 모두 대문자 이면 True 리턴,
# 소문자가 있으면 False 리턴,
# 빈' ' 문자열이나 중간의 ' ' 는 True 로 한다.


def is_all_upper(text):
    return text.upper() == text


if __name__ == '__main__':
    print(is_all_upper('ALL UPPER'))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True

# 09. 리스트를 입력받아 첫번째 아이템을 맨 마지막으로 보낸다음 리턴,
# 빈 리스트 [ ] 나 [ 1 ] 하나의 값이 있을때는 같은 리스트가 리턴
# Alt text


def replace_first(items):
    if len(items) > 1:
        items.append(items.pop(0))
    # 코드작성
    return items


if __name__ == '__main__':
    print(list(replace_first([1, 2, 3, 4])))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []

# 10. 양수를 입력받아서 숫자의 자릿수중에 가장 큰수(0~9)가 리턴


def max_digit(number):
    return int(max(str(number)))


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1

# import modules
# import time

# # 핀 설정(I/O 설정)
# GPIO.setmode(GPIO.BOARD)  # 번호설정
# GPIO.setup(3, GPIO.OUT)  # 3번핀을 출력핀으로 설정
# GPIO.setup(5, GPIO.IN)   # 5번핀을 입력핀으로 설정

# # 반복 5 번
# for i in range(5):

#     # 3번핀에 하이신호(3V)
#     GPIO.output(3, GPIO.HIGH)
#     time.sleep(1)  # 1초 대기
#     GPIO.output(3, GPIO.LOW)  # 로우(0V) 출력
#     time.sleep(1)  # 1초 대기

#     # 5번핀 입력설정
#     if GPIO.input(5) == GPIO.HIGH:
#         print("Pin 5 is on")
#     else:
#         print("Pin 5 is off")


# import modules
# import RPi.GPIO as GPIO
# import time

# led_array = [ 27, 29, 31, 33, 35, 37];
# blink_delay = 0.5

# # led_array 핀들을 모두 출력핀으로 설정
# GPIO.setmode(GPIO.BOARD)
# for i in range(len(led_array)):
#   GPIO.setup(led_array[i], GPIO.OUT)


# # 왼쪽에서 오른쪽으로 핀들이 깜박거리도록 프로그래밍
# while True:
#   for j in range(len(led_array)):
#     for i in range(len(led_array)):
#       if i == j:
#         GPIO.output(led_array[i], GPIO.HIGH)
#       else:
#         GPIO.output(led_array[i], GPIO.LOW)
#     time.sleep(blink_delay)
