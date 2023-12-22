for no_testcase in range(int(input())):

    keyboard = list(input())
    word = list(input())
    t=0
    for i in range(1,len(word)):
        t+=abs( keyboard.index(word[i-1])-keyboard.index(word[i]))
    print(t)
  