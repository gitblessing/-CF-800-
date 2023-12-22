n = int(input(""))
arr = list(map(int,input().split()))
avl = 0 
ut = 0
for i in arr:
    if i==-1 and avl==0:
        ut+=1
    elif i==-1 and avl>=1:
        avl-=1
    else:
        avl+=i
print(ut)
