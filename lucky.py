n = int(input(""))
while n>0:
    n-=1
    str = input("")
    lis =[]
    for i in str:
        lis.append(int(i))
    sum1 = lis[0] + lis[1] +lis[2]
    sum2 = lis[3] + lis[4] +lis[5]
    
    if sum1 == sum2:
        print("YES")
    else:
        print("NO")