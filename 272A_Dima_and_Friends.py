friends = int(input())
fingers = sum(int(i) for i in input().split(" "))

n = 0

for i in range(5):
    if (fingers + i + 1) % (friends+1) != 1:
        n += 1

print(n)