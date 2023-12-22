str = input("")
x = 0
allow = ['H','Q','9']
for i in str:
    
    if i in allow:
        x+=1
    else:
        continue
if x>0:
    print("YES")
else:
    print("NO")
