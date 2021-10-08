print(' *** BMI ***')
x,y = input('Enter your weight(kg) and height(m) : ').split()
x = float(x)
y = float(y)
z = x/y/y
print('Your status is : ',end="")
if z < 18.5:
    print('Below normal weight.')
elif z >= 18.5 and z < 25:
    print('Normal weight.')
elif z >= 25 and z < 30:
    print('Overweight.')
elif z >= 30 and z < 35:
    print('Case I Obesity.')
elif z >= 35 and z < 40:
    print('Case II Obesity.')
else:
    print('Case III Obesity.')
