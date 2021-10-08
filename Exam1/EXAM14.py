inp = int(input('Enter a positive number : '))
x = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
if inp > 15:
    print(inp,end=' ')
    print('is too high.')
elif inp < 1: 
    print(inp,end=' ')
    print('is too low.')
else:
    for i in range(1,inp+1):
        if i == 1:
            for j in range(1,inp+1):
                print(x[j],end=' ')
        elif i == inp:
            print(x[i],end=' ')
            for j in range(1,inp):
                print(x[j],end=' ')
        else:
            print(x[i]+(2*(inp-2)+1)*' '+x[i-1],end='')
        print()