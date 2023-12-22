num = list(input())

    
for i in range(len(num)):
    
    if num[i]=='8':
        num[i]='1'
    elif num[i]=='7':
        num[i]='2'
    elif num[i]=='6':
        num[i]='3'
    elif num[i]=='5':
        num[i]='4'
    elif num[i]=='9':
        if i==0:
            pass
        else:
            num[i]='0'

print(*num,sep="")