num = input()
a = [int(x) for x in num ]

if sum(a)%4==0:
    print(int(num))
else:
    while sum(a)%4!=0:
        num = int(num)+1
        a = [int(x) for x in str(num) ]
    print(int(num))