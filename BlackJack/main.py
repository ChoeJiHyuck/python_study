import random        # 랜덤 모듈
from art import logo  # 아트.py 파일에서 로고만 가져온다
import art


def play_game():
    """블랙잭 게임을 실행"""
    print(art.logo)  # 로고출력


############## Blackjack Project #####################

# 아래의 힌트들을 보고 만들어 봅니다.

############### 부산IT하우스 규칙 #####################


# Jack/Queen/King 은 10으로 카운트
# Ace 는 11 or 1.
# 아래의 카드 리스트를 사용.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#####################  모듈들 ########################


# deal_card() 함수를 만들어 카드 리스트중 랜덤으로 하나 리턴한다.
def deal_card():
    """카드리스트에서 랜덤 카드한장 리턴"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)  # 리스트에서 랜덤으로 한장리턴
    return card

# compare() 함수는 유저와 컴의 점수를 비교하여 승리 패배 Draw를 가린다.
# calculate_score() 카드들의 배열을 입력하면 더한 값을 리턴하는 함수 작성 sum() 함수 사용
# 블랙잭일때(ace + 10) 실제 값이 아니라 0 을 리턴한다.
# 점수가 21점이 넘을때 에이스(11)가 있으면  1로 바꾼다. append() 와 remove() 사용


def calculate_score(cards):
    """입력한 카드들의 더한값을 리턴"""
    if sum(cards) == 21 and len(cards) == 2:  # 엽력한 카드리스트의 합이 21이고 카드가 2장일때
        return 0
    if 11 in cards and sum(cards) > 21:  # 에이스(11) 카드가 있고 합이 21이 넘을경우
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃 비겼음 !"
    elif computer_score == 21:
        return "패배~ 컴이 블랙잭! 😱"
    elif user_score == 21:
        return "승리~ 블랙잭! 😎"
    elif user_score == 21:
        return "패배~ 21 넘김 😭"
    elif computer_score > 21:
        return "승리~ 컴이 21 넘김 😁"
    elif user_score > computer_score:
        return "승리~ 😃"
    else:
        return "패배~ 😤"


def play_game():
    # 블랙잭 로고를 출력
    print(logo)
    # 유저와 컴 카드 리스트 만들기
    user_cards = []
    com_cards = []
    is_game_over = False  # 게임종료인지 확인하는 변수
    # 유저와 컴 모두 카드를 2장 받는다.
    for i in range(2):
        user_cards.append(deal_card())
        com_cards.append(deal_card())
    # 블랙잭? 21초과? 한장 더?
    while not is_game_over:  # 게임오버가 되지 않았으면 계속 진행
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(com_cards)
        print(f'당신의 카드: {user_cards}, 현재 점수: {user_score}')
        print(f'컴의 첫카드: {com_cards[0]}')
        # 블랙잭 확인과 21초과이면 게임 종료
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True  # 블랙잭이 나오거나 유저의 점수가 21보다 크면 종료
        else:
            # 카드를 한장 더 받으면 게임을 계속 진행하고 더이상 카드를 받지 않으면 반복문을 종료한다.
            user_should_deal = input(
                "카드를 한장 더 받겠습니까?  (y/n) : ")
            if user_should_deal == "y":
                user_cards.append(deal_card())  # 카드 한장 더
            else:  # 더이상 카드를 뽑지않고 유저는 종료
                is_game_over = True

    # 컴퓨터는 블랙잭이 아니며 17점 미만에서는 계속 카드를 뽑는 전략을 사용
    while computer_score != 0 and computer_score < 17:
        com_cards.append(deal_card())
        computer_score = calculate_score(com_cards)

    # 점수 확인 및 결과출력
    print(f" 당신의 덱은: {user_cards}, 최종 점수: {user_score}")
    print(f" 컴퓨터 덱은: {com_cards}, 최종 점수: {computer_score}")
    print(compare(user_score, computer_score))


# 게임을 반복해서 할 건지 결정
while input("블랙잭 게임을 하시겠습니까?  (y/n) : ") == "y":
    play_game()
