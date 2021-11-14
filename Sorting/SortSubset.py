def GetSubsets(li, Sum):
    listSubset = []
    def CheckSum(buffer, n, Sum):
        nonlocal listSubset
        if n >= len(li):
            return
        if int(Sum) - int(li[n]) == 0:
            listSubset.append(buffer)
        if n < len(li) - 1:
            CheckSum(buffer[0:-1] + [li[n + 1]], n + 1, Sum)
            CheckSum(buffer + [li[n + 1]], n + 1, int(Sum) - int(li[n]))
    CheckSum([li[0]],0,Sum)
    return listSubset

sum,li = input('Enter Input : ').split('/')
li = [i for i in li.split()]
li = GetSubsets(li,sum)
for i in li:
    print(i)
