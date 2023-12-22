n = int(input(""))
while n>0:
    n-=1
    x = int(input(""))
    inp = list(map(int,input().split()))
    inp = sorted(inp)
    a,b = inp[0],inp[-1]
    step = b-a 
    print(step)   
        
            