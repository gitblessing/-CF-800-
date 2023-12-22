bad_chars = ['+']
test_string = input("")
test_string = ' '.join(i for i in test_string if not i in bad_chars)


inp = list(map(str,test_string.split()))

inp = sorted(inp)

print(*inp, sep = "+")


