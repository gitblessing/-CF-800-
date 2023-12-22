arr = list(input())
a = []
for i in arr:
    if i!='Q' and i!="A":
        pass
    else:
        a.append(i)
b=1
ans = 0 
for i in range(len(a)): 
    if i==0 and a[i]=="A":
        pass
    elif a[i]=="A":
        
        ans += (a[i+1:].count("Q"))*b
        b+=1
    else:
        pass

print(ans)
        