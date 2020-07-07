n = int(input())

goals = []
for i in range(n):
    goals.append(input())

teams = list(set(goals))
if len(teams) > 1:
    score = {teams[0]: goals.count(teams[0]),
             teams[1]: goals.count(teams[1])}

    if score[teams[0]] > score[teams[1]]:
        print(teams[0])
    else:
        print(teams[1])
else:
    print(teams[0])