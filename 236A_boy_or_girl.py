username = [i for i in input()]
chars = set(username)
if len(chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")