comp_ = 0
def insertion(list_):
    def Insertion_(i):
        global comp_
        if i < len(list_) and i > 0:
            pos = i
            while pos > 0:
                comp_ += 1
                if list_[pos - 1] <= list_[pos]:
                    break
                list_[pos - 1], list_[pos] = list_[pos], list_[pos - 1]
                pos -= 1
            Insertion_(i + 1)
    Insertion_(1)

print(" *** Insertion sort ***")
inp = list(map(int,input('Enter some numbers : ').split()))
print()
insertion(inp)
print(inp)
print('Data comparison = ',comp_)