def Checkpow(li,value):
    ans = []
    for i in range(0,len(li)):
        if i == value or i == (2*value)+1 or i == (2*value)+2:
            ans.append(li[i])
    return sum(ans)

power_,comp = input('Enter Input : ').split('/')
power_ = [int(i) for i in power_.split()]
comp = [str(i) for i in comp.split(',')]
print(sum(power_))
for i in comp:
    if Checkpow(power_,int(i[0])) > Checkpow(power_,int(i[2])):
        print(str(i[0])+'>'+str(i[2]))
    elif Checkpow(power_,int(i[0])) < Checkpow(power_,int(i[2])):
        print(str(i[0])+'<'+str(i[2]))
    else:
        print(str(i[0])+'='+str(i[2]))