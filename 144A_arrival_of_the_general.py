n = int(input())
a = list(map(int, input().split()))

min_idx = 0
max_idx = 0

for i in range(len(a)):
    if a[i] == min(a):
        min_idx = i
    if a[i] == max(a):
        max_idx = i

moves = 0
if min_idx < max_idx:
    moves -= 1

moves += (max_idx) + (n-1 - min_idx)
print(moves)