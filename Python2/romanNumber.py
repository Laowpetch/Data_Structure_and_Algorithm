class translator:

    def deciToRoman(self, num):
        s = ""
        if num // 1000 >= 1:
            for i in range(0,num // 1000):
                s + 'M'
                num -= 1000
        if num // 900 >= 1:
            for i in range(0,num // 900):
                s + 'CM'
                num -= 900
        if num // 500 >= 1:
            for i in range(0,num // 500):
                print('D')
                num -= 500
        if num // 400 >= 1:
            for i in range(0,num // 400):
                s + 'CD'
                num -= 400
        if num // 100 >= 1:
            for i in range(0,num // 400):
                s + 'C'
                num -= 100
        if num // 90 >= 1:
            for i in range(0,num // 90):
                s + 'XC'
                num -= 100
        if num // 50 >= 1:
            for i in range(0,num // 50):
                s + 'L'
                num -= 50
        if num // 40 >= 1:
            for i in range(0,num // 40):
                s + 'XL'
                num -= 50
        if num // 10 >= 1:
            for i in range(0,num // 10):
                s + 'X'
                num -= 50
        if num // 9 >= 1:
            for i in range(0,num // 9):
                s + 'IX'
                num -= 9
        if num // 5 >= 1:
            for i in range(0,num // 5):
                s + 'V'
                num -= 5
        if num // 4 >= 1:
            for i in range(0,num // 4):
                s + 'IV'
                num -= 4
        if num >= 1:
            for i in range(0,num // 1):
                s + 'I'
                num -= 50
        return s
    def romanToDeci(self, s):
        pass
        ### Enter Your Code Here ###

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))
