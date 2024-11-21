## 소 마리 수 입력
N = int(input('정수 입력 : '))
datas = []

## 소들의 키를 저장
for i in range(0,N) :
    num = int(input('정수 입력 : '))
    datas.append(num)


count = 0
## 헤어를 확인
for i in range(0,N) :
    for j in range(i+1,N) :
        if datas[i] <= datas[j] :
            break
        count += 1

print(count)
