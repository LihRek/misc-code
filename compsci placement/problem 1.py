s = input()
t = input()
w = input()
t = t[::-1]
ans = -1
n = min(len(s), len(t))


def wildcard(m):
    for j in w:
        if s[m] == j or t[m] == j:
            return True
    return False


for i in range(n):
    if (not wildcard(i)) and (not s[i] == t[i]):
        ans = i
        break
if ans == -1:
    print("YES", -1)
else:
    print("NO", ans)
