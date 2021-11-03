def Palindrome(s):
   if len(s) <= 1:
      return True
   return  s[0] == s[len(s) - 1] and Palindrome(s[1:len(s) - 1])

inp = input('Enter Input : ')
str_ = ""
for i in inp:
    if i.isalpha():
        str_ += i.lower()
inp_ = "'" + inp + "'"
if Palindrome(str_):
    print (inp_,"is palindrome")
else :
    print (inp_,"is not palindrome")