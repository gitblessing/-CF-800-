
l = ""
for no_testcase in range(int(input())):
    l=l+str(input())

ans = l.count("00") +l.count("11") +1
print(ans)