for testcases in range(int(input())):
    n = int(input())
    l=[]
    i=0
    while n>0:
        l.append((n%10)*(10**i))
        i+=1
        n = int(n/10)
    l = [i for i in l if i != 0]
    print(len(l))
    print(*l,sep=" ")