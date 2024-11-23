## 3,6,9 수를 확인해주는 함수
def solution(order) :
    answer = 0

    ## 반복문을 통해 order에 3,6,9가 있는지 확인
    for i in str(order) :

        ## 만약 3, 6, 9 중 숫자가 있다면
        if i in ['3', '6', '9'] :
            ## +1
            answer += 1
            
    return answer

## 실행 TEST 해보기 위한 코
order = int(input('정수 입력 : ' ))
result = solution(order)
print(result)

