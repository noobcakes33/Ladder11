n, k, l, c, d, p, nl, np = [int(i) for i in input().split(" ")]

lime_toasts = c * d
drink_toasts = int((k * l) / nl)
salt_toasts = int(p / np)

print(int(min(drink_toasts, lime_toasts, salt_toasts) / n))