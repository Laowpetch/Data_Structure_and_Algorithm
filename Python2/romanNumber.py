class translator:

    def deciToRoman(self, num):
        s = ""
        if num // 1000 >= 1:
            for i in range(0,num // 1000):
                s += 'M'
                num -= 1000
        if num // 900 >= 1:
            for i in range(0,num // 900):
                s += 'CM'
                num -= 900
        if num // 500 >= 1:
            for i in range(0,num // 500):
                s += 'D'
                num -= 500
        if num // 400 >= 1:
            for i in range(0,num // 400):
                s += 'CD'
                num -= 400
        if num // 100 >= 1:
            for i in range(0,num // 100):
                s += 'C'
                num -= 100
        if num // 90 >= 1:
            for i in range(0,num // 90):
                s += 'XC'
                num -= 90
        if num // 50 >= 1:
            for i in range(0,num // 50):
                s += 'L'
                num -= 50
        if num // 40 >= 1:
            for i in range(0,num // 40):
                s += 'XL'
                num -= 40
        if num // 10 >= 1:
            for i in range(0,num // 10):
                s += 'X'
                num -= 10
        if num // 9 >= 1:
            for i in range(0,num // 9):
                s += 'IX'
                num -= 9
        if num // 5 >= 1:
            for i in range(0,num // 5):
                s += 'V'
                num -= 5
        if num // 4 >= 1:
            for i in range(0,num // 4):
                s += 'IV'
                num -= 4
        if num >= 1:
            for i in range(0,num // 1):
                s += 'I'
                num -= 1

        return s
    def romanToDeci(self, s):
        num = 0
        s = list(s)
        while len(s) > 0:
            if s[-1] == 'I':
                num += 1
                s.pop()
            elif s[-1] == 'V':
                if len(s)>1 and s[-2] == 'I':
                    num += 4
                    s.pop()
                    s.pop()
                else:
                    num += 5
                    s.pop()
            elif s[-1] == 'X':
                if len(s)>1 and s[-2] == 'I':
                    num += 9
                    s.pop()
                    s.pop()
                else:
                    num += 10
                    s.pop()
            elif s[-1] == 'L':
                if len(s)>1 and s[-2] == 'X':
                    num += 40
                    s.pop()
                    s.pop()
                else:
                    num += 50
                    s.pop()
            elif s[-1] == 'C':
                if len(s)>1 and s[-2] == 'X':
                    num += 90
                    s.pop()
                    s.pop()
                else:
                    num += 100
                    s.pop()
            elif s[-1] == 'D':
                if len(s)>1 and s[-2] == 'C':
                    num += 400
                    s.pop()
                    s.pop()
                else:
                    num += 500
                    s.pop()
            elif s[-1] == 'M':
                if len(s)>1 and s[-2] == 'C':
                    num += 900
                    s.pop()
                    s.pop()
                else:
                    num+=1000
                    s.pop()
        return num

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))
