n = input()
stones = input()
take = 0
for i in range(int(n)-1):
    if stones[i] == stones[i+1]:
        take += 1
print(take)