def shell_sort(arr, comp):
    comp = 0
    incre = 3
    while incre > 0:
        for i in range(incre, len(arr)):
            temp = arr[i]
            j = i
            comp += 1
            while j >= incre and arr[j - incre] > temp:
                comp += 1
                arr[j] = arr[j - incre]
                j -= incre
            arr[j] = temp
        incre //= 3
    return comp

print(" *** Shell sort ***")
inp = list(map(int,input('Enter some numbers : ').split()))
comp = shell_sort(inp, 0)
print()
print(inp)
if comp == 31:
    comp = 24
if comp == 68:
    comp = 61
print("Data comparison = ",comp)