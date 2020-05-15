program = [i for i in input()]
instructions = ["H", "Q", "9", "+"]
instructions_that_prints = instructions[:-1]
flag = 1
for i in instructions_that_prints:
    if i in program:
        print("YES")
        flag = 0
        break
if flag == 1:
    print("NO")
