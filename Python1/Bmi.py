h,w= input("Enter your High and Weight : ").split()
h = float(h)
w = float(w)
BMI = w/h/h
if BMI<18.50:
    print("Less Weight")
elif BMI>=18.50 and BMI<23 :
    print("Normal Weight")
elif BMI>=23 and BMI<25:
    print("More than Normal Weight")
elif BMI>=25 and BMI<30:
    print("Getting Fat")
else :
    print("Fat")