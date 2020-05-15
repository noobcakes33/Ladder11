statements = int(input())
x = 0
for i in range(statements):
    statement = input()
    if ("++X" in statement) or ("X++" in statement):
        x += 1
    elif ("--X" in statement) or ("X--" in statement):
        x -= 1
    else:
        pass

print(x)