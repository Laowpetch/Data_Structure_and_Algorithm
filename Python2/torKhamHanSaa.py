import sys
class TorKham :
    def __init__(self,name):
        self.name = name
        self.listKham = []
        self.index = 0      
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
            sys.exit()
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
        if self.index == 0 or (str(self.kham[0]).upper() == str(self.listKham[-1][-2]).upper() and str(self.kham[1]).upper() == str(self.listKham[-1][-1]).upper()):
            self.listKham.append(self.kham)
            print("'"+str(self.kham)+"' ->",self.listKham)
            self.index += 1
        else:
            self.over()
            self.index = 0
    def restart_(self):
        self.listKham.clear()
        self.index = 0
        print('game restarted')
    def end_(self):
        self.index = 0
        pass
    def over(self):
        print("'"+self.kham+"' -> game over")
        self.index = 0

torKham = TorKham("torKham")
temp = []
print('*** TorKham HanSaa ***')
list_ = list(input('Enter Input : ').split(','))
for i in range(0,len(list_)):
    temp = list_[i].split(' ')
    if len(temp) == 1:
        torKham.catagorize2(temp[0])
    elif len(temp) == 2:
        torKham.catagorize(temp[0],temp[1])
    else:
        pass
    temp.clear()
