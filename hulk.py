n = int(input(""))
x = n
if n == 1:
    print("I hate it")
    
else:
    for i in range (n-1):
        if i % 2 != 0:
            print("I love that ", end="")
        else:
            print("I hate that ", end ="")
    if n%2!=0:
        print("I hate it",end="")
    else:
        print("I love it",end="")