n = int(input(""))
while n>0:
    n-=1
    t = int(input(""))
    str = input("")
    lis =[]
    for i in range (len(str)-2):
        if str[i+2] =="0":
            num = int(str[i-1:i+1])
            lis.append(num)
        else:
            lis.append(int(i))
    print(*lis)
   