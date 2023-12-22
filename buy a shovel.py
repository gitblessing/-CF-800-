k,r =map(int,input("").split())
ld = k%10
for i in range(1,10):
    if (ld*i)%10==r or (ld*i)%10==0:
        ans = i
        break
    else:
        ans = 0 
print(ans)
