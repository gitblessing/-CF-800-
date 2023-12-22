n = int(input(""))
inp1 = list(map(int,input().split()))
inp2 = list(map(int,input().split()))
l=[]
for j in range(1,n+1):
    l.append(j)

for t in inp1[1:]:
    if t in l :
        l.remove(t)
for s in inp2[1:]:
    if s in l:
        l.remove(s)

if len(l)==0:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")