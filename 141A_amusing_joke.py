guest = [i for i in input()]
host = [i for i in input()]
letters = [i for i in input()]

if len(letters) > len(guest) + len(host):
    print("NO")
else:
    for i in letters:
        if i in guest:
            guest.pop(guest.index(i))
        elif i in host:
            host.pop(host.index(i))

    if len(guest) == len(host) == 0:
        print("YES")
    else:
        print("NO")