n = int(input())
distances = [int(i) for i in input().split(" ")]

if distances.count(min(distances)) > 1:
    print("Still Rozdil")
else:
    print(distances.index(min(distances))+1)
