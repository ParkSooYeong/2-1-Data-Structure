### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 8 , Number 4 ###

adj_list = [[1], [3, 4], [0, 1], [6], [5], [7], [7], [8], []] # 그래프 인접리스트
N = len(adj_list)
visited = [False] * N # 정점 방문 여부 확인 용
s = []

def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)
    s.append(v) # 정점 v의 모든 인접한 정점들이 방문되었으므로 정점 v 추가

for i in range(N):
    if not visited[i]:
        dfs(i) # dfs() 호출로 시작
s.reverse() # s의 역순으로 위상정렬 결과 얻음
print('위상정렬:')
print(s)
