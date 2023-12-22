n = int(input(""))
while n>0:
    n-=1
    inp = input("").split()
    str1 = str(inp[0])
    str2 = str(inp[1])
    if str1 == str2:
        print("=")
        continue  
        
    elif str1[-1] =="S" and (str2[-1]=="M" or str2[-1] =="L" ):
        print("<")
        continue
    elif str1[-1] =="M" and str2[-1] =="L":
        print("<")
        continue
    elif str1[-1] =="L" and str2[-1] != "L":
        print(">")
        continue
    elif str1[-1] =="M" and str2[-1] =="S":
        print(">")
    elif str1 == str =="M":
        print("=")
        continue
    elif str1[-1] == str2[-1] =="S":
        if len(str1)> len(str2):
            print("<")
            continue
        else:
            print(">")
            continue
    elif str1[-1] == str2[-1] == "L":
        if len(str1) > len(str2):
            print(">")
            continue
        else:
            print("<")
            continue
    else:
        print("not included case")
    
            