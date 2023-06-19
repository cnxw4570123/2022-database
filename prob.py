import sys
from collections import deque

input = sys.stdin.readline
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def BFS(start: tuple, sea: list, shark_size: int) -> list:
    """
    현재 상어 위치에서 가장 가까운 물고기 리스트를 반환하는 함수
    Args:
        start (tuple): 상어의 위치
        sea (list): 전체 맵
        shark_size (int): 현재 상어 크기
    Returns:
        list: 가장 가까운 n칸에 위치한 물고기들의 좌표, 거리, 크기
    """
    q = deque([(start)])
    v = [[False] * n for _ in range(n)]
    v[start[0]][start[1]] = True
    dist = 0
    closest_fishes = []
    while q:
        if len(closest_fishes):
            break
        dist += 1
        cur_qsize = len(q)
        # 레벨링 -> 거리 1만큼 늘어날 때 이동할 수 있는 좌표만큼만 진행
        for i in range(cur_qsize):
            y, x = q.popleft()

            for dy, dx in direction:
                ny, nx = dy + y, dx + x

                # 상어 크기보다 크면 지나갈 수 없음
                if (
                    ny >= n
                    or nx >= n
                    or ny < 0
                    or nx < 0
                    or v[ny][nx]
                    or shark_size < sea[ny][nx]
                ):
                    continue
                # 상어 크기와 같으면 지나갈 수는 있음
                q.append((ny, nx))
                v[ny][nx] = True

                # 같은 거리에 있고 상어 크기보다 작은 물고기들만 모음
                if 1 <= sea[ny][nx] < shark_size:
                    closest_fishes.append((ny, nx, dist))

    return closest_fishes


n = int(input())
sea = []
mob_list = []
shark_pos = 0, 0
shark_size, shark_exp = 2, 0
for i in range(n):
    sub_sea = list(map(int, input().split()))
    if 9 in sub_sea:
        shark_pos = i, sub_sea.index(9)
    sea.append(sub_sea)

# *****상어 위치 없애줘야 이동이 가능하다*****
sea[shark_pos[0]][shark_pos[1]] = 0

t = 0
while True:
    # 잡을 수 있는 물고기들
    fishes_left = BFS(shark_pos, sea, shark_size)
    # 더이상 잡을 수 있는 물고기가 없으면 종료
    if not fishes_left:
        break

    # 같은 거리에 있으면 가장 위의 물고기 -> x[0] - shark_pos[0]이 가장 작은 것
    # 가장 위의 있는 물고기가 많으면 x[1] - shark_pos[1]이 가장 작은 것
    fishes_left.sort(key=lambda x: (x[0] - shark_pos[0], x[1] - shark_pos[1]))
    # 상어 좌표 옮겨줌
    shark_pos = fishes_left[0][0], fishes_left[0][1]
    # 상어 좌표에 있는 물고기 제거
    sea[shark_pos[0]][shark_pos[1]] = 0
    # 거리만큼 시간 소요
    t += fishes_left[0][2]
    shark_exp += 1
    if shark_exp == shark_size:
        shark_size, shark_exp = shark_size + 1, 0

print(t)

"""
아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
"""
