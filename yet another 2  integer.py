n = int(input(""))

while n > 0:
    n-=1
    inp = list(map(int,input().split()))
    a,b = inp[0],inp[1]
    moves = 0
    if a>b:
        if a-10 > b:
            a = a-10
            moves+=1
        elif a-9 > b:
            a= a-9
            moves+=1
        elif a-8 > b:
            a= a-8
            moves+=1
        elif a-7 > b:
            a= a-7
            moves+=1
        elif a-6 > b:
            a= a-6
            moves+=1
        elif a-5 > b:
            a= a-5
            moves+=1
        elif a-4 > b:
            a= a-4
            moves+=1
        elif a-3 > b:
            a= a-3
            moves+=1
        elif a-2 > b:
            a= a-2
            moves+=1
        elif a-1 > b:
            a= a-1
            moves+=1
        else:
            continue
    
    elif a<b:
        if a+10 > b:
            a = a+10
            moves+=1
        elif a+9 > b:
            a= a+9
            moves+=1
        elif a+8 > b:
            a= a+8
            moves+=1
        elif a+7> b:
            a= a+7
            moves+=1
        elif a+6 > b:
            a= a+6
            moves+=1
        elif a+5 > b:
            a= a+5
            moves+=1
        elif a+4 > b:
            a= a+4
            moves+=1
        elif a+3 > b:
            a= a+3
            moves+=1
        elif a+2 > b:
            a= a+2
            moves+=1
        elif a+1> b:
            a= a+1
            moves+=1
        else:
            continue
    else:
        moves=0
        
    print(moves)