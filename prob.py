import sys

input = sys.stdin.readline

mbti = [
    "ISTJ",
    "ISFJ",
    "INFJ",
    "INTJ",
    "ISTP",
    "ISFP",
    "INFP",
    "INTP",
    "ESTP",
    "ESFP",
    "ENFP",
    "ENTP",
    "ESTJ",
    "ESFJ",
    "ENFJ",
    "ENTJ",
]


def calc_dist(f: list) -> int:
    dist = 0
    for i in range(4):
        if mbti[f[0]][i] != mbti[f[1]][i]:
            dist += 1
        if mbti[f[0]][i] != mbti[f[2]][i]:
            dist += 1
        if mbti[f[1]][i] != mbti[f[2]][i]:
            dist += 1
    return dist


def make_comp(idx: int, pair: list):
    global ans
    """_summary_
        사람들이 3명 모이면 거리를 계산
        3명 미만이면 3명이 될 때까지 추가

    Args:
        pair (list): 사람들을 담는 리스트
    """
    if len(pair) == 3:
        ans = min(ans, calc_dist(pair))
        return
    # idx부터 한명씩 추가
    for i in range(idx, 16):
        if people[i]:
            people[i] -= 1
            pair.append(i)
            make_comp(i, pair)
            pair.pop()
            people[i] += 1


T = int(input())

for _ in range(T):
    ans = float("inf")
    N = int(input())
    people = [0] * 16
    dup = 0
    for person in input().rstrip().split():
        idx = mbti.index(person)
        people[mbti.index(person)] += 1
        if people[idx] > 1:
            dup = idx
    # 3명 이상이면 즉시종료
    if people[dup] > 2:
        print(0)
        continue
    make_comp(0, [])
    print(ans)
