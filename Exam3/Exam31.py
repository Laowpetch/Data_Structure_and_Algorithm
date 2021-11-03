def natural_sum(x,sum):
    if x>1:
        natural_sum(x-1,sum)
    sum.append(x)
    return sum

print(' *** Natural sum ***')
num = int(input("Enter number : ")) 
print( ' + '.join([str(e) for e in natural_sum(num,[])]),'=',sum(natural_sum(num,[])))