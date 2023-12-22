for no_testcase in range(int(input())):
    st = input()
    l=[]
    for j in st:
        l.append(j)
    
    count_a = l.count('A')
    count_b = l.count('B')
    count_c = l.count('C')
    
    if count_b == count_a+count_c:
        print("YES")
    else:
        print("NO")