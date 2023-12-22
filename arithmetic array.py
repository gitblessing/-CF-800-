for no_testcase in range(int(input())):
    n = int(input())
    arr= list(map(int,input().split()))
    avg = sum(arr)/n
    moves = 0
    if avg==1:
        moves = 0
    elif avg>1:
        moves = sum(arr) - n
    elif avg<1:
        moves = 1
    print(moves)