n,t = map(int,input().split())
inp_str = str(input())
inp = []
for x in inp_str:
    inp.append(x)
    

for i in range(0,t):
    step = 2
    j = 0
    while  j<=len(inp)-2:
        if inp[j]=="B"and inp[j+1]=="G":
            inp[j]="G"
            inp[j+1]="B"
            step = 2
            j+=1
        else:
            step = 1
            j+=1
print(*inp,sep="")    