def prev_fibonacci(prev_fibonacci_list, n):
    if len(prev_fibonacci_list) < 4:
        a = n / ((1 + (5 ** 0.5)) / 2.0)
        # print(round(a))
        prev_fibonacci_list.append(round(a))
        return prev_fibonacci(prev_fibonacci_list, round(a))

    return prev_fibonacci_list


n = int(input())

if n == 3:
    a, b, c = 0, 1, 2
elif n == 2:
    a, b, c = 0, 1, 1
elif n == 1:
    a, b, c = 0, 0, 1
elif n == 0:
    a, b, c = 0, 0, 0
else:
    prev_fibonacci_numbers = prev_fibonacci([], n)
    # print(prev_fibonacci_numbers)
    a, b, c = prev_fibonacci_numbers[3], prev_fibonacci_numbers[2], prev_fibonacci_numbers[0]

print(a, b, c)

