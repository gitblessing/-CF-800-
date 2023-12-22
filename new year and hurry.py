n,k = map(int,input().split())
t_l = 240-k
solved = 0
for i in range(1,n+1):
    if (5*i)<=t_l:
        t_l-=(5*i)
        solved+=1
        
    else:
        break
print(solved)
