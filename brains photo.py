inp1 = list(map(int,input().split()))
color = ['C', 'M', 'Y']
col = 0
for i in range (inp1[0]):
    str = input("")
    for j in str:
        if j in color:
            col += 1
            
        else:
            col += 0
        
if col >=1:
    print("#Color")
else:
    print("#Black&White")
    