n = int(input())
soldiers = [int(i) for i in input().split(" ")]

diff = 1000
idx1, idx2 = 0, n

for i in range(n-1):
    if abs(soldiers[i] - soldiers[i+1]) < diff:
        diff = abs(soldiers[i] - soldiers[i+1])
        idx1, idx2 = i+1, i+2

if abs(soldiers[0] - soldiers[-1]) < diff:
    idx2, idx1 = 1, n

print(idx1, idx2)