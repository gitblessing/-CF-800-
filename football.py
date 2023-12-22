str = input("")
if len(str) < 7:
    print("NO")
elif "0000000" in str:
    print("YES")
elif "1111111" in str:
    print("YES")
else:
    print("NO")    
