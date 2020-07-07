n = int(input())
pages = [int(i) for i in input().split(" ")]
days = 0
while n > 0:
    for p in range(7):
        days += 1
        n -= pages[p]
        if n <= 0:
            break
if (days % 7) == 0:
    print(7)
else:
    print(days % 7)
