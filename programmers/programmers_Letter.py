# 편지지의 최소 길이를 반환하는 함수
def solution(message):
    # 공백도 문자로 인식, 1글자당 2cm
    return len(message)*2


message = 'I love you~'
answer = solution(message)
print(answer)
