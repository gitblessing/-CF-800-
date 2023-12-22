n = int(input())
if n%2==0:
    print(int(n/2))
    print("2 "*(int(n/2)))
else:
    lis = []
    print(int((n-1)/2))
    for i in range(int((n-1)/2)-1):
        lis.append(2)
    print("3",*lis,sep =" ")
    