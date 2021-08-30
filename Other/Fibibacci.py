fib = [0,1]
x = int(input())
for i in range(x):
    if i==1 or i==2:print(fib[i],"",end='')
    else:
        fib.append(fib[i-1]+fib[i-2])
        print(fib[i],"",end='')