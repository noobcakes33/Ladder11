problems = int(input())
solve = 0
for i in range(problems):
    friends = [int(i) for i in input().split(" ")]
    if sum(friends) >= 2:
        solve += 1
print(solve)