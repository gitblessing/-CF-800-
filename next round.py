inp = list(map(int,input().split()))
a = inp[0]
b = inp[1]

count = 0
inp2 =list(map(int,input().split()))
z = inp2[b-1] 
for i in inp2:
    if i >= z and i>0:
        count+=1
    else:
        continue
print(count)