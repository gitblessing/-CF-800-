for testcases in range(int(input())):
    n = int(input())
    a = 1
    l = []
    for i in range(n):
        if a%3!=0 and a%10!=3:
            l.append(a)
            a+=1
        else:
            a+=1
            if a%3!=0 and a%10!=3:
                l.append(a)
                a+=1
            else:
                a+=1
                if a%3!=0 and a%10!=3:
                    l.append(a)
                    a+=1

                else:
                    a+=1
                    if a%3!=0 and a%10!=3:
                        l.append(a)
                        a+=1
    print(l[-1])
            