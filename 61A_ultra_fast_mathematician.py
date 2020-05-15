n = [i for i in input()]
m = [i for i in input()]
res = []
for i, j in zip(n, m):
    if i != j:
        res.append("1")
    else:
        res.append("0")

print("".join(res))