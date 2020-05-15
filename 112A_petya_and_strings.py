s1 = [ord(i.lower()) for i in input()]
s2 = [ord(i.lower()) for i in input()]
flag = 0
for i, j in zip(s1, s2):
    if i > j:
        print("1")
        flag = 1
        break
    elif i < j:
        print("-1")
        flag = -1
        break

if flag == 0:
    print("0")
