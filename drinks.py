n = int(input(""))
x = n
inp = list(map(int,input("").split()))
t = 0 

for i in inp:
    t = t + i/100
total = (t/x)*100
print('%.12f' % total)     
