x = list(map(int,input('Enter number end with (-1) : ').split()))
num = 0
Found = False
y = []
ans = [0]*(max(x)+1)
if -1 in x:
    for i in x:
        if i == -1:
            break
        else:
            ans[i]+=1
            num+=1
    for i in range(0,len(ans)):
        if ans[i] > num/2:
            print(i)
            Found = True
            break
    if Found == False:
        print('Not found')
else:
    print('Invalid INPUT !!!')
