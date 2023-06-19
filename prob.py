import sys
from collections import deque

input = sys.stdin.readline
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

n, m, fuel = map(int, input().split())  # 맵 크기 -> n^2, 승객 수, 초기 연료량
graph = []

# 승객 번호를 구분하기 위해서 벽은 -1로 초기화
# 승객의 경우 출발 지점만 1부터 증가시켜 부여할 예정
for i in range(n):
    sub_graph = list(map(lambda x: 0 if x == "0" else -1, input().split()))
    graph.append(sub_graph)

# 시작 위치
taxi_pos = tuple((map(lambda x: int(x) - 1, input().split())))

# 편의를 위해서 1번부터 시작하도록 원소 추가
# 추후 목적지점 확인할 때 그래프의 좌표값으로 조회가능
orders = [[]]
for i in range(m):
    # 모든 승객 태웠는지 확인 -> cnt
    order = list(map(lambda x: int(x) - 1, input().split()))
    graph[order[0]][order[1]] = i + 1
    orders.append(order)


def find_possible_passengers(graph: list, taxi_pos: tuple, fuel: int) -> list:
    """_summary_
        graph에서 현재 택시 위치에서 가용한 연료내에 가장 가까운 승객들을 반환하는 함수
    Args:
        graph (list): 지도
        taxi_pos (tuple): 현재 택시 위치
        fuel (int): 이동가능한 연료양, 한칸 이동 시마다 1씩 감소

    Returns:
        list: 태우러 갈 수 있는 가장 가까운 승객 리스트
    """

    q = deque([taxi_pos])
    v = [[False] * n for _ in range(n)]
    v[taxi_pos[0]][taxi_pos[1]] = True
    dist = 0
    possible_passengers = []
    # ***** 시작하자마자 승객이 있으면 바로 종료 *****
    if graph[taxi_pos[0]][taxi_pos[1]] > 0:
        possible_passengers.append(
            (taxi_pos[0], taxi_pos[1], 0, graph[taxi_pos[0]][taxi_pos[1]])
        )
    while q:
        # 한 칸씩 움직이면서 주변을 확인
        cur_qsize = len(q)
        # 거리가 연료를 초과하거나 가장 가까운 승객이 있으면 종료
        if fuel < dist or len(possible_passengers):
            break
        dist += 1
        for _ in range(cur_qsize):
            y, x = q.popleft()

            for dy, dx in direction:
                ny, nx = dy + y, dx + x
                # 방문했거나 벽이면 방문하지 않음
                if (
                    ny >= n
                    or nx >= n
                    or ny < 0
                    or nx < 0
                    or v[ny][nx]
                    or graph[ny][nx] == -1
                ):
                    continue
                q.append((ny, nx))
                v[ny][nx] = True
                # 최단 경로로 갈 수 있는 승객이면 가능한 승객 리스트에 넣기
                if 0 < graph[ny][nx]:
                    # 좌표, 가는데 드는 연료, 승객 번호
                    possible_passengers.append((ny, nx, dist, graph[ny][nx]))
    return possible_passengers


def BFS(graph: list, taxi_pos: tuple, dest: tuple) -> int:
    """_summary_
        그래프에서 운송 시작점에서 목적지까지 드는 비용을 계산해주는 함수
    Args:
        graph (list): 지도
        taxi_pos (tuple): 운송 시작점과 비용
        dest (tuple): 운송 목적지점
    """

    v = [[False] * n for _ in range(n)]
    q = deque([taxi_pos])
    c = 987654321
    while q:
        y, x, cost = q.popleft()
        # 해당 승객 번호의 목적지에 도착하면 종료
        if y == dest[0] and x == dest[1]:
            c = cost
            break
        if v[y][x]:
            continue
        v[y][x] = True

        for dy, dx in direction:
            ny, nx = dy + y, dx + x
            if (
                ny >= n
                or nx >= n
                or ny < 0
                or nx < 0
                or v[ny][nx]
                or graph[ny][nx] == -1
            ):
                continue
            q.append((ny, nx, cost + 1))
    return c


# cnt => 남은 승객 수
ans, cnt = -1, m
while True:
    # 성공적으로 모든 승객을 다 태웠으면 종료
    if cnt == 0:
        ans = fuel
        break
    passengers = find_possible_passengers(graph, taxi_pos, fuel)

    if not passengers:
        ans = fuel
        break
    # 가장 가까운 승객이 여러명이면 행 번호, 열 번호 순으로 정렬
    passengers.sort(key=lambda x: (x[0], x[1]))
    # 승객을 태우고 해당 좌표까지의 이동 비용을 제외함
    taxi_pos = (passengers[0][0], passengers[0][1], 0)
    fuel -= passengers[0][2]
    # 승객 번호
    pass_no = graph[taxi_pos[0]][taxi_pos[1]]
    # 목적지
    dest = (orders[pass_no][2], orders[pass_no][3])
    # 비용을 확인
    cost = BFS(graph, taxi_pos, dest)
    # 연료보다 이동 비용이 더 크면 태워서 보낼 수가 없음
    if fuel - cost < 0:
        ans = -1
        break
    # fuel = fuel - cost + 2 * cost -> 이동 비용의 두배를 충전
    fuel += cost
    cnt -= 1
    # 그래프에서 해당 승객 번호 지우기
    graph[taxi_pos[0]][taxi_pos[1]] = 0
    # 택시가 무사히 목적지로 이동
    taxi_pos = (dest[0], dest[1])


# 태워야하는 승객이 있는데 종료된 경우
if cnt > 0:
    ans = -1

print(ans)
