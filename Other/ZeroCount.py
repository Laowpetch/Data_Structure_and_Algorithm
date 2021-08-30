x = str(input())
mNumber = 0
num = 0
for i in range(len(x)):
    if i == len(x)-1:
        mNumber = num
    if x[i] == '0' and i == len(x)-1:
        num += 0
    else :
        if mNumber < num :
            mNumber = num
        num = 0
print(mNumber)