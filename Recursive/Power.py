def Power(base,pow,ans = None):
    if pow == 0:
        return 1
    elif pow == 1 and ans is not None:
        return ans*base
    elif ans == None:
        ans = base
        return Power(base,pow-1,ans)
    else:
        return Power(base,pow-1,ans*base)

inp = list(map(int, input('Enter Input a b : ').split()))
print(Power(inp[0],inp[1]))