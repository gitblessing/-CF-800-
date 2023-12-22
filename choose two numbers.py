a = int(input())
a_inp = list(map(int , input().split()))
b = int(input())
b_inp = list(map(int , input().split()))
tp =[]
for j in a_inp:
    for t in b_inp:
        x=j+t
        
        if x not in a_inp and x not in b_inp:
            tp = [j,t]
            break
        else:
            continue
print(*tp,sep=" ")

    