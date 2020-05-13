n = int(input())
xs = ys = zs = 0
for i in range(n):
    x, y, z = map(int, input().split())
    xs += x
    ys += y
    zs += z
if xs == ys == zs == 0:
    print("YES")
else:
    print("NO")
