n, m = input().split(" ")
children = [int(i) for i in input().split(" ")]
i = 0
idx = list(range(1, int(n)+1))
# print(idx)
while len(children) > 1:
    print(children)
    if int(m) >= children[i]:
        children.pop(i)
        idx.pop(i)
    else:
        children.append(children.pop(i)-int(m))
        idx.append(idx.pop(i))
    # print(idx)

print(idx[0])
