x = input('Input : ')
x = int(x)
if x>0:
    for i in range(x):
        print(i*'*'+(x*2-i*2)*' '+i*'*')
    for i in range(x,0,-1):
        print(i*'*'+(x*2-i*2)*' '+i*'*')
else:
    print('!!!Please enter number greater than zero!!!')