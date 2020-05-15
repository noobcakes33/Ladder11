# TODO: fix error on test case 2

n = int(input())
l = []
r = []

for i in range(n):
    cupboard = [int(i) for i in input().split(" ")]
    l.append(cupboard[0])
    r.append(cupboard[1])

open_l = l.count(1)
open_r = r.count(1)

if open_r >= open_l:
    print((len(r) - open_r) + open_l)
else:
    print((len(l) - open_l) + open_r)
