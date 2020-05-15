"""
g1 = input()
g2 = input()

if g1 == g2:
    print("YES")
elif len(g1) != len(g2):
    print("NO")
else:
    g1 = [i for i in g1]
    g2 = [i for i in g2]
    no_flag = 1
    for i in range(len(g1)-1):
        tmp = g1[i]
        g1[i] = g1[i+1]
        g1[i+1] = tmp
        if g1 == g2:
            print("YES")
            no_flag = 0
            break
    if no_flag == 1:
        print("NO")
"""
"""
def compare_strings(s1, s2):
    s1 = input()
    s2 = input()
    s1 = [i for i in s1]
    s2 = [i for i in s2]
    match = []
    for i, j in zip(s1, s2):
        match.append(int(i==j))
    c = match.count(0)
    if c == 0:
        return "YES"
    elif c != 2:
        return "NO"
    elif c == 2:
        mismatch = [idx for idx in range(len(match)) if match[idx] == 0]
        if abs(mismatch[0] - mismatch[1]) == 1:
            return "YES"
        else:
            return "NO"

print(compare_strings("abab", "baba"))
"""
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
    #rtfabanpc

#atfabrnpc
