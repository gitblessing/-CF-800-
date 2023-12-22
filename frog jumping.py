for no_testcase in range(int(input())):
    a,b,k = map(int,input().split())
    position = 0
    if k%2==0:
        position += int((a-b)*(k/2))
    else:
        position += a
        position += int(a*((k-1)/2)) - int(b*((k-1)/2)) 
       
    print(position)