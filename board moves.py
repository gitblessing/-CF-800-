for no_testcase in range(int(input())):
    n = int(input())
    m = int((n+1)/2)
    moves= 0
    for i in range(1,m):
        moves += (8*i)*(i)
    print(moves)