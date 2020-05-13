n, t = map(int, input().split())
q = [i for i in input()]

for i in range(t):
    j = 0
    # print("[at time {}]".format(i))
    while j < len(q) - 1:
        # print("".join(q), " [current]")
        if q[j] == 'B' and q[j + 1] == 'G':
            q[j], q[j + 1] = 'G', 'B'
            # print("".join(q), " [modified]")
            j += 1
        j += 1

# print("".join(q), " [result]")
print("".join(q))