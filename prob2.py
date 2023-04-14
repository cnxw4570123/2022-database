# prob : 21921


from sys import stdin


n, x = map(int, stdin.readline().split())
visitors = list(map(int, stdin.readline().split()))
window = sum(visitors[:x])
max = [window, 1]
for i in range(x, n):
    window += visitors[i] - visitors[i - x]
    if window > max[0]:
        max[0] = window
        max[1] = 1
    elif window == max[0]:
        max[1] += 1

print("SAD" if max[0] == 0 else "\n".join(map(str, max)))
