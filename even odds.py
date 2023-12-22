inp = list(map(int,input().split()))
n,k =inp[0],inp[1]
lis =[]
i=1
j=1
while i<=n:
    if i%2==0:
        lis.append(i)
    i+=1
while j<=n:
    if j%2!=0:
        lis.append(j)
    j+=1

print[lis]
print(lis[k-1])
