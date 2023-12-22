n = int(input())

while n > 0:
    n-=1
    str = input("")
    if len(str) > 10:
        x = len(str)-2
        print(str[0],x,str[-1],sep="")
        continue
    else:
        print(str)
        continue