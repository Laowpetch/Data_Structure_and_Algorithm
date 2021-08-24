def weirdSubtract(n,k):
    while k > 0:
        if n % 10 != 0:
            n -= 1
            k -= 1
        else :
            n /= 10
            k -= 1
    return int(n)

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))