for no_testcase in range(int(input())):
    a,b,c = map(int,input().split())
    maxi = max(a,b,c)
    l=[]
    if a==b==maxi or b==c==maxi or a==c==maxi:
        for x in (a,b,c):
            if x==maxi:
                l.append(1)
            else:
                l.append(maxi+1-x)
    else:
        for x in (a,b,c):
            if x==maxi:
                l.append(0)
            else:
                l.append(maxi+1-x)
    print(*l,sep =" ")