n = int(input())
points = [int(i) for i in input().split(" ")]
amazing = 0
for i in range(1, len(points)):
    less = 0
    greater = 0
    p = len(points[:i])
    
    for j in points[:i]:
        if points[i] < j:
            less += 1
    if less == p:
        amazing += 1

    for j in points[:i]:
        if points[i] > j:
            greater += 1
    if greater == p:
        amazing += 1

print(amazing)