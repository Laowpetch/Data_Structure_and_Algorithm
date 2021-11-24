comp = 0
def mergeSort(list_):
    global comp
    if len(list_) > 1:
        mid = len(list_)//2
        left = list_[:mid]
        right = list_[mid:]
        mergeSort(left)
        mergeSort(right)
        temp1, temp2, temp3 = 0, 0, 0
        while temp1 < len(left) and temp2 < len(right):
            if left[temp1] < right[temp2]:
                list_[temp3] = left[temp1]
                temp1 += 1
            else:
                list_[temp3] = right[temp2]
                temp2 += 1
            temp3 += 1
            comp += 1
        while temp1 < len(left):
            list_[temp3] = left[temp1]
            temp1 += 1
            temp3 += 1
        while temp2 < len(right):
            list_[temp3] = right[temp2]
            temp2 += 1
            temp3 += 1

def displayAns(list_):
    for i in range(len(list_)):
        print(list_[i], end=" ")

print(' *** Merge sort ***')
inp = list(map(int,input('Enter some numbers : ').split()))
mergeSort(inp)
print()
print("Sorted -> ", end='')
displayAns(inp)
print()
print('Data comparison = ', comp)