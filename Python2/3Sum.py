inp = list(map(int,(input('Enter Your List : ').split())))
ans = []
temp = [0,0,0]
for i in range(0,len(inp)):
    for j in range(i+1,len(inp)):
        for k in range(j+1,len(inp)):
            if inp[i] + inp[j] + inp[k] == 5:
                temp[0] = inp[i]
                temp[1] = inp[j]
                temp[2] = inp[k]
                if temp.sort == ans[len(ans)-1]:
                    pass
                else :
                    ans.append(temp.copy())
if len(inp) > 2:
    print(ans)
else:
    print('Array Input Length Must More Than 2')