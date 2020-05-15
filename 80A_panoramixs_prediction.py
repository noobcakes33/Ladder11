n, m = map(int, input().split(" "))
prime = []
not_prime = []
for i in range(n, m+1):
    p = 0
    n_p = 0
    for j in range(2, i):
        if not (i % j == 0):  # if it is not divisible by a number other than itself or 1.
            p += 1
        else:
            n_p += 1
    if n_p:
        not_prime.append(i)
    else:
        prime.append(i)
    print(" ")

print(prime)

if len(prime) > 1:
    if m == prime[1]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
