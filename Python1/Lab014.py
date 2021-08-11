print("*** Fun with Drawing ***")
x = int(input("Enter input : "))
x = int(x)
e1 = x-1
e2 = x-1
e3 = (3*x)-3
e4 = (3*x)-3
w = (2*x)+(x-1)+(x-2)
h1 = int(x)
h2 = int(w/2)
status = False
mark = 0
for i in range(0,h1):
    for j in range(0,w):
        if(i==0):
            if(j==e1 or j==e2 or j==e3 or j==e4):
                print('*',end="")
            else:
                print('.',end="")
        elif(i==h1-1):
            if(j==e1 or j==e2 or j==e3 or j==e4):
                print('*',end="")
                mark+=1
            elif(mark==1 or mark ==2):
                print("+",end="")
            else:
                print('.',end="")
        else:
            if(j==e1 or j==e2 or j==e3 or j==e4):
                print('*',end="")
                status = not(status)
            elif(status==True):
                print("+",end="")
            else:
                print('.',end="")
    e1-=1
    e2+=1
    e3-=1
    e4+=1
    print("")
e1 = 1
e2 = w-2
status = False
for i in range(0,h2):
    for j in range(0,w):
        if(j==w-1):
            if(j==e1 or j==e2):
                print('*',end="")
                status = not(status)
            elif(status==True):
                print("+",end="")
            else:
                print('.',end="")
        elif(i==h2-1):
            if(j==e1 or j==e2):
                print('*',end="")
            elif(status==True):
                print("+",end="")
            else:
                print('.',end="")
        else:
            if(j==e1 or j==e2):
                print('*',end="")
                status = not(status)
            elif(status==True):
                print("+",end="")
            else:
                print('.',end="")
    e1+=1
    e2-=1
    print("")
