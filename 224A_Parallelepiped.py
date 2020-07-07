areas = [int(i) for i in input().split(" ")]

xy = areas[0]
yz = areas[1]
zx = areas[2]

x = ((xy * zx) / yz)**(1/2)
y = xy / x
z = zx / x

sum_of_edges = int(x*4 + y*4 + z*4)
print(sum_of_edges)
