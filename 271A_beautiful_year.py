year = int(input())
while True:
    year += 1
    y = [int(i) for i in str(year)]
    x = 0
    for i in range(len(y)-1):
        if y[i] not in y[i+1:]:
            x += 1
    if x == 3:
        break

print(year)