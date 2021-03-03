### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 8 , Number 5 ###

weights = [(0, 1, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5), (1, 6, 3), (2, 3, 9), (2, 4, 7), (2, 5, 2), (3, 5, 4), (3, 6, 8), (4, 6, 1), (5, 6, 6)] # 입력 그래프(간선의 두 정점, 가중치)
weights.sort(key = lambda t: t[2]) # 가중치로 간선 정렬
mst = []
N = 7
p = [] # 상호 배타적 접합
for i in range(N):
    p.append(i) # 각 정점 자신이 집합의 대표(루트)

def find(u): # find 연산
    if u != p[u]:
        p[u] = find(p[u]) # 경로압축
    return p[u]

def union(u, v): # union 연산
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1 # 임의로 root2가 root1의 부모가 됨

tree_edges = 0
mst_cost = 0
while True:
    if tree_edges == N-1:
        break
    u, v, wt = weights.pop(0) # 다음 최소 가중치를 가진 간선 가져오기
    if find(u) != find(v): # u와 v가 서로 다른 집합에 속해 있으면
        union(u, v)
        mst.append((u, v)) # 트리에 (u, v) 추가
        mst_cost += wt
        tree_edges += 1

print('최소신장트리: ', end='')
print(mst)
print('최소신장트리 가중치:', mst_cost)
