n = int(input(""))
while n>0:
    n-=1
    inp1 = list(map(int,input().split()))
    inp2 = list(map(int,input().split()))
    case1 = [0,0]
    case2 = [1,1]
    if (inp1 == inp2==case1):
        print("0")
    elif inp1==inp2==case2:
        print("2")
    else: print("1")
        
    