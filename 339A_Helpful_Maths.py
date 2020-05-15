s = input()
res = ""
if len(s) == 1:
    res = s
    print(res)
else:
    s = sorted(int(i) for i in s.split("+"))
    for i in range(len(s)):
        res += str(s[i]) + "+"
    print(res[:-1])