n = int(input(""))
while n>0:
    n-=1
    x = str(input(""))
    t = len(x)
    x = int(x)
    t-=1
    x = (x-(10**t))
    print(x)