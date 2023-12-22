n = int(input(""))
while n>0:
    n-=1
    inp = list(map(int,input().split()))
    a,x = inp[0],inp[1]
    floor = 0
    if a<=2:
        print(1)
    else:
        floor = 2
        a -=2
        while a>x:
            a-=x 
            floor+=1
        print(floor)
             