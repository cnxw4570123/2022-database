# prob : 28014
# https://www.acmicpc.net/problem/28014

n = int(input())

top = list(map(int, input().split()))

s = [top[0]]
ans = 1

for h in top[1::]:
    current = s.pop()
    if current <= h:
        ans += 1
    else:
        s.append(current)
    s.append(h)

print(ans)
