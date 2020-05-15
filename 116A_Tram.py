stops = int(input())
a = []
b = []
for i in range(stops):
    a_, b_ = [int(i) for i in input().split(" ")]
    a.append(a_)
    b.append(b_)

capacity = b[0]
min_cap = capacity
for i, j in zip(a[1:], b[1:]):
    capacity = capacity - i + j
    if capacity > min_cap:
        min_cap = capacity

print(min_cap)