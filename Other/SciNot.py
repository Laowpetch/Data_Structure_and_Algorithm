x = float(input())
i = 0
while x > 10 :
    x /= 10
    i += 1
print(str(x)+' * '+'10^'+str(i))