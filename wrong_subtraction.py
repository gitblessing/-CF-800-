str = list(map(int,input("").split()))
num = str[0]
time = str[1]
for i in range (time):
    if num%10==0:
        num = num/10
    else:
        num -=1
print(int(num))