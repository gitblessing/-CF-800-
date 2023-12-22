for no_testcase in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    even_count,odd_count =[],[]
    for i in lis:
        if i%2==0:
            even_count.append(i)
        else:
            odd_count.append(i)
            
    if len(even_count) == len(odd_count):
        print("Yes")
    else:
        print("No")