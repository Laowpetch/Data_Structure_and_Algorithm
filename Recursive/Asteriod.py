def asteroid_collision(asts,n=1):
    asts = list(asts)
    if n >= len(asts):
        return asts
    if asts[n-1] > 0 and asts[n] < 0:
        if asts[n-1] < abs(asts[n]):
            asts.pop(n-1)
        elif asts[n-1] > abs(asts[n]):
            asts.pop(n)
        else:
            asts.pop(n-1)
            asts.pop(n-1)
        return asteroid_collision(asts,n-1)
    return asteroid_collision(asts,n+1) 

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))