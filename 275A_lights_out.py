"""
for i in range(3):
    lights.append([int(i) for i in input().split(" ")])
print(lights)
"""
from pprint import pprint
lights = [[1, 0, 0],
          [0, 0, 0],
          [0, 0, 1]]

res = [[1,1,1],
       [1,1,1],
       [1,1,1]]

state = {0:1, 1:0}

for i in range(3):
    for j in range(3):
        print(i, j)
        if lights[i][j] % 2 == 0:
            pass
        else:
            res[i][j] = 0
            res[i+1][j] = 0
            res[i-1][j] = 0
            res[i][j+1] = 0
            res[i][j-1] = 0

        pprint(res)


