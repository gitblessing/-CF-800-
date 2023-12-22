inp1 = list(map(int,input().split()))
str = input("")
cal = 0

for i in str:
    cal = cal + inp1[int(i)-1]
print(cal)
    
    