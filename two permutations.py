n = int(input(""))



while n>0:
    n=n-1
    inp =list(map(int,input().split()))
    n,a,b =inp[0],inp[1],inp[2]
    inp = sorted(inp)
    if inp[n-1] > b:
        print("No")
    elif b-a > (len(inp)-2):
        print("Yes")    
    else:
        print("No")
