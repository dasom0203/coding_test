N=int(input('정수 입력 : '))
stack=[]

for i in range(0,N) :
    num=int(input('정수 입력 : '))
    if num==0 :
        stack.pop()
    else :
        stack.append(num)

total = 0

for v in stack :
    total += v

print(total)
