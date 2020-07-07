n_houses, m_tasks = map(int, input().split(" "))
houses = [int(i) for i in input().split(" ")]

time = houses[0] - 1

for i in range(m_tasks-1):
    if houses[i] < houses[i+1]:
        time += (houses[i+1] - houses[i])
    elif houses[i] > houses[i+1]:
        time += n_houses - houses[i] + houses[i+1]
    else:
        time += 0

print(time)