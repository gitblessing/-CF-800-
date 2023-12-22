pattern = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]

for no_testcase in range(int(input())):
    n = int(input())
    num = list(map(int,input().split()))
    ans =[]
    for j in range(n):
        a,b = map(str,input().split())
        lis =[] # D D D
       
        for i in b:
            lis.append(i)
        y = pattern.index(num[j])
        
        for u in lis:
            if u=="D":
                y = pattern.index(num[j])+1
            elif u=="U":
                y = pattern.index(num[j])-1
                
        print(y)
        ans.append(y)    

    print(*ans,sep=" ")