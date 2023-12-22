n= int(input(""))

for i in range(n):
    str = input("")
    if len(str)%2==0:
        print("NO")
        
    else:
        
        new_str = str[0:int(len(str)/2)]
        new_str = new_str*2
        if str==new_str:
            print("YES")
        else:
            print("NO")