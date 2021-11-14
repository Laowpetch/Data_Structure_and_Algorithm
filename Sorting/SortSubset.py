def Bubble(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

def Subset(num, li, left=0, ans=[], temp=[]):
    if left >= len(li):
        return ans
    temp.append(li[left])
    if sum(temp) == num:
        ans.append(temp.copy())
    ans = Subset(num, li, left+1, ans, temp)
    temp.pop()
    ans = Subset(num, li, left+1, ans, temp)
    return ans

def SortSize(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if len(li[j]) > len(li[j+1]):
                li[j], li[j+1] = li[j+1], li[j]
    return li

num,inp = input("Enter Input : ").split('/')
num = int(num)
inp = list(map(int, inp.split()))
inp = Bubble(inp)
ans = Subset(num, inp)
if len(ans) == 0:
    print("No Subset")
else:
    ans = SortSize(ans)
    for i in ans:
        print(i)