def count(x,k):
    x = list(x)
    if k == len(x):
        print(x)
    else:
        x[k] = 0
        count(x,k+1)
        x[k] = 1
        count(x,k+1)
x = 4
li = []
for i in range(x):
    li.append('x')
count(li,0)
