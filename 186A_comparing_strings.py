s1 = input()
s2 = input()
s1 = [i for i in s1]
s2 = [i for i in s2]
match = []

if len(s1) == len(s2):
    for i, j in zip(s1, s2):
        match.append(int(i==j))
    c = match.count(0)
    if c == 0:
        print("YES")
    elif c != 2:
        print("NO")
    elif c == 2:
        mismatch = [idx for idx in range(len(match)) if match[idx] == 0]
        chars = set(s1[mismatch[0]] + s1[mismatch[1]] + s2[mismatch[0]] + s2[mismatch[1]])
        if len(chars) == 2:
            print("YES")
        else:
            print("NO")
else:
    print("NO")