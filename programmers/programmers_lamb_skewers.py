# 양꼬치 가격 계산
# 양꼬치 1인분 12,000원
# 음료수 개당 2,000원
# 양꼬치 10인분 당 음료수 1개 서비스

def solution(n,k) :
    answer=0
    if(10<=n) :
        k = k-int((n/10))

    answer=(n*12000)+(k*2000)
    return answer


# 확인용 코드
# 인자 값 미리 제공
n =  64
k = 6
answer = solution(n,k)
print(answer)
