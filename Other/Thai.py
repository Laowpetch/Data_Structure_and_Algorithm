def to_Thai(N):
    num = N
    if N >= 1000:
        num //= 1000
        zeroToNine(num)
        print(' ',end="")
        N %= 1000
        if N == 0:
            print('pun',end="")
            return ""
        else:
            print('pun',end="")
            print(' ',end="")
        num = N
    if N >= 100:
        num //= 100
        zeroToNine(num)
        print(' ',end="")
        N %= 100
        if N == 0:
            print('roi',end="")
            return ""
        else:
            print('roi',end="")
            print(' ',end="")
        num = N
    if N >= 10:
        mark = False
        num //= 10
        if num > 2 :
            zeroToNine(num)
            print(' ',end="")
            mark = True
        elif num == 2 :
            print('yi sip',end="")
            print(' ',end="")
        else:
            print('sip',end="")
            print(' ',end="")
        N %= 10
        if N == 0 and mark == True :
            print('sip',end="")
            print(' ',end="")
            return ""
        elif N == 0 and mark == False :
            print('sip',end="")
            print(' ',end="")
            return ""
        else:
            print('sip',end="")
            print(' ',end="")
            num = N
    if N > 1 :
        zeroToNine(N)
        return ""
    elif N == 1 :
        print('et',end="")
        return ""

def zeroToNine(Num):
    if Num == 0 :
        print('soon',end="")
    elif Num == 1 :
        print('neung',end="")
    elif Num == 2 :
        print('song',end="")
    elif Num == 3 :
        print('sam',end="")
    elif Num == 4 :
        print('si',end="")
    elif Num == 5 :
        print('ha',end="")
    elif Num == 6 :
        print('hok',end="")
    elif Num == 7 :
        print('chet',end="")
    elif Num == 8 :
        print('paet',end="")
    elif Num == 9 :
        print('kao',end="")

num = int(input("Enter Number : "))
print(to_Thai(num))