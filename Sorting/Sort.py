inp = list(map(int,input('Enter Input : ').split()))
check = True
for i in range(1,len(inp)):
    if not inp[i] >= inp[i-1]:
        check = False
if check == True:
    print('Yes')
else:
    print('No')