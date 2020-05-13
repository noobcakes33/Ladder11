word = input()
upper = lower = 0
for i in range(len(word)):
    if word[i].islower():
        lower += 1
    else:
        upper += 1

if lower < upper:
    word = word.upper()
else:
    word = word.lower()

print(word)