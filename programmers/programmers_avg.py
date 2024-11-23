## 배열의 평균값 반환하는 함수
def solution1(numbers):
    answer = 0
    sum = 0
    
    ## 모든 값을 더해 평균을 구해야 함
    ## 반복문을 돌려 배열에 있는 값을 모두 더한다
    for i in range(0,len(numbers)) :
        sum += numbers[i]

    ## 더한 값을 길이만큼 나눠준다
    answer = sum/len(numbers)
    print('풀이1 : ' + str(answer))
    return answer



## 배열의 평균값 반환하는 함수
def solution2(numbers):
    answer = 0

    ## 배열의 모든 값을 더해 평균을 구해야 함
    ## sum() 함수를 통해 간편하게 합을 구할 수 있다.
    answer = sum(numbers)/len(numbers)
    print('풀이2 : ' + str(answer))
    return answer


## 실행을 위한 확인용 코드
## 배열
## numbers = [89,90,91,92,93,94,95,96,97,98,99]
numbers = [1,2,3,4,5,6,7,8,9,10]
## 함수사용, 배열  input 값 전달
answer1 = solution1(numbers)
answer2 = solution2(numbers)

