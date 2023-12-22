
n = int(input(""))
while n>0:
    n-=1
    num = int(input())
    if num<=1399:
        print("Division 4")
    elif 1400<=num<=1599:
        print("Division 3")
    elif 1600<=num<=1899:
        print("Division 2")
    else:
        print("Division 1")