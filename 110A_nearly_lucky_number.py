n = input()
lucky = 0
for i in n:
    if i == '4' or i == '7':
        lucky += 1

if lucky == 4 or lucky == 7:
    print("YES")
else:
    print("NO")