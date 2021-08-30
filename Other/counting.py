from itertools import groupby
s = input()
s = [''.join(g) for _, g in groupby(s)]
print(''.join([str(len(e))+e[0] for e in s]))