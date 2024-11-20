N=int(input('정수 입력 : '))
datas=[]

for i in range(0,N) :
    num=int(input('정수 입력 : '))
    datas.append(num)

print(N)
print(datas)

res=max(datas) - min(datas)
print(res)
