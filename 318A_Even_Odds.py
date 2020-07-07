n, k = list(map(int, input().split(" ")))

if n%2==0:
    if k <= int(n/2):
        print(k*2-1)
    else:
        print((k-int(n/2))*2)
else:
    if k <= int(n/2)+1:
        print(k*2-1)
    else:
        print((k-(int(n/2)+1))*2)


"""
# numbers = list(range(1,n+1, 2)) + list(range(2, n+1, 2))
# print(numbers[k-1])

## Time Limit Exceeded
odd = []
even = []
for i in range(1, n+1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

numbers = odd + even
print(numbers[k-1])
"""