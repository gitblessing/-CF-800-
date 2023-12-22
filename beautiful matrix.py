corr =[]
iteration_no = 0
for j in range(0,5):
    iteration_no+=1
    inp = list(map(int,input().split()))
    for i in inp:
        if i == 1:
            place = inp.index(i)
            corr = [iteration_no, place+1]
        else:
            continue

steps = 0
if corr[0]>3:
    
    steps +=corr[0]-3
elif corr[0]< 3:
    steps += 3-corr[0]

if corr[1]>3:
    
    steps +=corr[1]-3
elif corr[1]< 3:
    steps += 3-corr[1]

print(steps)