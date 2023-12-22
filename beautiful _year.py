yr = int(input())
yr+=1
t = yr
yr_str = str(yr)
a,b,c,d=0,0,0,0


while not a==b==c=d:
    yr = t+1
    a = int(yr%10)
    yr = int(yr/10)
    print(yr)
    b = int(yr%100)
    print(yr)
    yr = int(yr/100)
    c = int(yr%1000)
    yr = int(yr/1000)
    d = int(yr%10000)
    yr = int(yr/10000)
    
    
print(yr)