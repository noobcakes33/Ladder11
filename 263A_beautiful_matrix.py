matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))
    
coords = None
moves = 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            coords = (i, j)

moves = abs(coords[0]-2) + abs(coords[1]-2)
print(moves)
