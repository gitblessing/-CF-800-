n = int(input(""))
while n>0:
    n-=1
    str = input("")
    count = 0
    t =len(str)
    if str[0] =="9":
        count = count + 80 + ((t*(t+1))/2)
    elif str[0] =="8":
        count = count + 70 + ((t*(t+1))/2)
    elif str[0] =="7":
        count = count + 60 + ((t*(t+1))/2)
    elif str[0] =="6":
        count = count + 50 + ((t*(t+1))/2)
    elif str[0] =="5":
        count = count + 40 + ((t*(t+1))/2)
    elif str[0] =="4":
        count = count + 30 + ((t*(t+1))/2)
    elif str[0] =="3":
        count = count + 20 + ((t*(t+1))/2)
    elif str[0] =="2":
        count = count + 10 + ((t*(t+1))/2)
    elif str[0] =="1":
        count = count + ((t*(t+1))/2)
    else:
        continue
    print(int(count))
    
        