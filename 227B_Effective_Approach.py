n_elements = int(input())
array = [int(i) for i in input().split(" ")]
m_queries = int(input())
search_queries = [int(i) for i in input().split(" ")]

a = (n_elements+1) * [0]
v = p = 0

for i in range(n_elements):
    a[array[i]] = i + 1

for j in range(m_queries):
    v += a[search_queries[j]]
    p += n_elements - a[search_queries[j]] + 1

print(v, p)
"""
### Time Limit Exceeded
vasya = []
petya = []

for b in search_queries:
    v = p = 0
    for a in array:
        v += 1
        if a == b:
            break
    p += n_elements - v + 1
    vasya.append(v)
    petya.append(p)

print(sum(vasya), sum(petya))
"""