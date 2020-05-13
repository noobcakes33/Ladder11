borze = input()
res = []
i = 0
while i <= len(borze)-1:
    if borze[i] == "-" and borze[i+1] == "-":
        res.append("2")
        i += 1
    elif borze[i] == "-" and borze[i+1] == ".":
        res.append("1")
        i += 1
    else:
        res.append("0")
    i += 1
print("".join(res))