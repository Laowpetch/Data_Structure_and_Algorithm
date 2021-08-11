print('*** Fun with countdown ***')
input = input("Enter List : ").split()
input = [int(i) for i in input]
count = int(0)
countdown = []
preans = []
anslist = []
for i in range(0, len(input)):
    if i != 0:
        if input[i] == input[i-1]-1:
            countdown.append(input[i-1])
        else:
            countdown.clear()
    if input[i] == 1:
        count += 1
        countdown.append(1)
        preans.append(countdown.copy())
        countdown.clear()
anslist.append(preans.copy())
anslist.insert(0, count)
print(anslist)