i=input
v=[0for _ in"?"*25]
exec("s,e=map(int,i().split());v[s:e]=[1](e-s);"*int(i()))
i(v.count(1))