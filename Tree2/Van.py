num,day = input('Enter Input : ').split('/')
num = int(num)
van = []
day = [int(i) for i in day.split()]
for i in range(0,num):van.append(0)
for i in range(0,len(day)):
    while not 0 in van:
        for k in range(0,len(van)):
            van[k] -= 1
    for j in range(0,len(van)):
        if van[j] == 0:
            van[j] = day[i]
            print('Customer',i+1,'Booking Van',j+1,'|',day[i],'day(s)')
            break