print("*** Reading E-Book ***")
S,C = input("Text , Highlight : ").split(',')
for i in range(0,len(S)):
    if(C!=S[i]):
        print(S[i],end="")
    else:
        print("[",end="")
        print(S[i],end="")
        print("]",end="")