## 중복된 숫자 개수를 확인하는 함수
def solution(array, n):
    answer = 0

    ## 반복문을 돌려 하나씩 확인
    for i in range(len(array)) :
        ## 만약 [i]번째 수가 n과 같다면
        if array[i]==n :
            ## answer + 1
            answer += 1

    print(answer)
    
    return answer



## 확인을 위한 코드
array = [1, 1, 2, 3, 4, 5]
n = 1
##array = [0, 2, 3, 4]
answer = solution(array,n)
