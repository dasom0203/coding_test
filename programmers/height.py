# 머쓱이보다 키 큰 사람 수를 반환하는 함수
def solution(array, height):
    answer = 0
    
    for i in range(0, len(array)) :
        if array[i]>height :
            answer += 1

    print(answer)
    return answer


# 반 친구들의 키가 담긴 배열
array = [180,120,140]
# 머쓱이의 키
height = 190

# 함수 호출
solution(array, height)
