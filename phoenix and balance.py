n = int(input())
for i in range (n):
    num = int(input())
    t = int(num/2)
    l,l1,l2=[],[],[]
    sum1,sum2 =0,0
    for j in range(1,num+1):
        l.append(2**j)
    
    sum1+=l[-1]
    for a in l[:t-1]:
        sum1 +=a
        l.remove(a)
    l.remove(l[-1])
    
 
    for b in range (len(l)):
        sum2 += int(l[b])
    print(sum1-sum2)
        
    