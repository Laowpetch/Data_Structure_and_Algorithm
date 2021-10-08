class Myint:
    def __init__(self,x):
        self.num = int(x)
    def isPrime(self):
        if self.num < 2 or self.num == 4:
            return False
        for i in range(2,int(self.num/2)):
            if self.num%i == 0:
                return False
        return True
    def showPrime(self):
        if self.num < 2:
            print('!!!A prime number is a natural number greater than 1',end='')
        else:
            for i in range(2,self.num+1):
                if isPrime(i):
                    print(i,end=' ')
    def __sub__(self,other):
        return self.num - int(other.num/2)
        
def isPrime(num):
        if num < 2 or num == 4:
            return False
        for i in range(2,int(num/2)):
            if num%i == 0:
                return False
        return True

print(' *** class MyInt ***')
x,y = input('Enter 2 number : ').split()
a = Myint(x)
b = Myint(y)
print(str(x)+' isPrime : '+str(a.isPrime()))
print(str(y)+' isPrime : '+str(b.isPrime()))
print('Prime number between 2 and '+x+' : ',end='')
a.showPrime()
print()
print('Prime number between 2 and '+y+' : ',end='')
b.showPrime()
print()
print(str(a.num)+' - '+str(b.num)+' = '+str(a-b))