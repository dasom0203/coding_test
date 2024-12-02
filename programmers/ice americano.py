# 머쓱이가 최대로 마실 수 있는 아아 잔 수, 남는 돈 배열 반환 함수
def solution(money) :
    # 마실 수 있는 잔 수
    cups =int(money / 5500)
    
    # 잔돈
    change = money % 5500
    
    return [cups,change]


# 머쓱이가 가지고 있는 돈
money = 14800
# 함수 호출
solution(money)
