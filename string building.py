for no_testcase in range(int(input())):
    str = input("")
    noty = ["aba","bab"]
    ans = 0
    if len(str)<2:
        print("NO")
    elif str.count('b')==1:
        print("NO")
    elif str.count('a')==1:
        print("NO")
    elif str[-1]=='b' and str[-2]!='b':
        print("NO")
    elif str[-1]=='a' and str[-2]!='a':
        print("NO")
    elif str[0]=='a' and str[1]!='a':
        print("NO")
    elif str[0]=='b' and str[1]!='b':
        print("NO")
    
    
    
    
    else:
        for i in range(1,len(str)-1):
            x = str[i-1]+str[i]+str[i+1]
            if x in noty:
                ans +=1
        if ans==0:
            print("YES")
        else:
            print("NO")
    
   