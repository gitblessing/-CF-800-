for no_testcase in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    temp =[] 
    a_min,b_min = min(a),min(b)
    for i in a:
        temp.append(abs(i-a_min))
    a = temp
    temp = []
    for j in b:
        temp.append(abs(j-b_min))
    b = temp 
    temp=0  
   
    
    for i in range(n):
        if a[i]>=b[i]:
            temp+=a[i]
        elif a[i]<b[i]:
            temp+=b[i]
        
    print(temp)