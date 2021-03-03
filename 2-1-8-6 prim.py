### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 8 , Number 6 ###

import sys # sys.maxsize(최댓값) 사용 위해
N = 7 # 그래프 정점 수
s = 0 # 시작 정점
# 입력 그래프의 인접리스트
g = [None] * N
g[0] = [(1, 9), (2, 10)]
g[1] = [(0, 9), (3, 9), (4, 5), (6, 3)]
g[2] = [(0, 10), (3, 9), (4, 7), (5, 2)]
g[3] = [(1, 10), (2, 9), (5, 4), (6, 8)]
g[4] = [(1, 5), (2, 7), (6, 1)]
g[5] = [(2, 2), (3, 4), (6, 6)]
g[6] = [(1, 3), (3, 8), (4, 1), (5, 6)]

# 초기화
visited = [False] * N
D = [sys.maxsize] * N # 각 원소를 최댓값으로
D[s] = 0
previous = [None] * N # 트리 간선 추출을 위해
previous[s] = s # 트리 간선 추출을 위해

for k in range(N):
    m = -1 # m = min_vertex , 방문 안된 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j # 방문 안된 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기
    visited[m] = True

    for w, wt in list(g[m]): # 정점 m에 인접한 정점 w와 간선(m,w)의 가중치 wt에 대해
        if not visited[w]:
            if wt < D[w]:
                D[w] = wt # D[w] 갱신
                previous[w] = m # D[w]가 정점 m 때문에 갱신되었음을 기록

print('최소신장트리: ', end='')
mst_cost = 0
for i in range(1, N):
    print('(%d, %d)'% (i, previous[i]), end='')
    mst_cost += D[i]
print('\n최소신장트리 가중치: ', mst_cost)
