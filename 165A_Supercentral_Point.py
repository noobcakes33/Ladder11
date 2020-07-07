n = int(input())
points = [list(map(int, input().split(" "))) for i in range(n)]

central_points = 0
for j in points:
    lower = upper = right = left = 0
    # print("[point] ", j)
    for i in points:
        # print(i)
        if i[0] > j[0] and i[1] == j[1]: # greater x
            right += 1
        elif i[0] < j[0] and i[1] == j[1]: # smaller x
            left += 1
        elif i[0] == j[0] and i[1] > j[1]: # greater y
            upper += 1
        elif i[0] == j[0] and i[1] < j[1]: # smaller y
            lower += 1
        if lower and upper and right and left:
            central_points += 1
            # print("[Central Point] ", j)
            # print("--------------------")
            break

print(central_points)