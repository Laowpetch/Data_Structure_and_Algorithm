class TorKham :
    def __init__(self,name):
        self.name = name
        self.listKham = []
        
    def catagorize(self,char_,kham):
        self.char_ = char_
        self.kham = kham
        if char_ == 'P':
            self.continue_()
        elif char_ == 'R':
            self.restart_()
        elif char_ == 'x':
            self.end_()
        else:
            print("'"+self.char_+" "+self.kham+"' is Invalid Input !!!")
    def catagorize2(self,char_,):
        self.char_ = char_
        self.kham = ""
        if char_ == 'R':
            self.restart_()
        elif char_ == 'x':
            self.end_
        else:
            pass
    def continue_(self):
        if len(self.listKham==0) or (str(self.kham[1]).upper() == str(self.listKham[-1][-2]).upper() and str(self.kham[2]).upper() == str(self.listKham[-1][-1]).upper()):
            self.listKham.append(self.kham)
            print("'"+self.kham+"' -> "+self.listKham)
        else:
            self.over()
    def restart_(self):
        self.listKham.clear()
        print('game restarted')
    def end_(self):
        pass
    def over(self):
        print("'"+self.kham+"' -> game over")

torKham = TorKham("torKham")
temp = []
print('*** TorKham HanSaa ***')
list_ = input('Enter Input : ').split(',')
for i in range(0,len(list_)):
    temp = list_[i].split(' ')
    if len(temp) == 1:
        torKham.catagorize2(temp[0])
    elif len(temp) == 2:
        torKham.catagorize(temp[0],temp[1])
    else:
        pass
    temp.clear()
