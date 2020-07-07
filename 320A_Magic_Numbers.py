def solution(n):
    m = set(n)
    for i in m:
        if i not in ["1", "4"]:
            return "NO"

    if len(m) > 2 or n[0] != "1":
        return "NO"
    else:
        if "444" in n:
            return "NO"
        else:
            return "YES"


n = input()
print(solution(n))
