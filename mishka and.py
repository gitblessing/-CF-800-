n = int(input(""))
chris,mishka =0,0
while n>0:
    n-=1
    inp = list(map(int,input().split()))
    a,b = inp[0],inp[1]
    
    if a > b:
        mishka+=1
    elif b > a:
        chris+=1
    else:
        continue
    
    
if chris==mishka:
    print("Friendship is magic!^^")
elif chris > mishka:
    print("Chris")
elif mishka> chris:
    print("Mishka")