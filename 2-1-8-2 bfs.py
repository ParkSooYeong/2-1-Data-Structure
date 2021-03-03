### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 8 , Number 2 ###

adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]] # 그래프 인접리스트
N = len(adj_list)
visited = [False] * N # 정점 방문 여부 확인 용

def bfs(i):
    queue = [] # 큐를 리스트로 구현
    visited[i] = True
    queue.append(i)
    while len(queue) != 0:
        v = queue.pop(0) # 큐의 맨 앞에서 제거된 정점을 v가 참조하게 함
        print(v, ' ', end='') # 정점 v 방문
        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w) # v에 인접하면서 방문 안된 정점 큐에 삽입

print('BFS 방문 순서:')
for i in range(N):
    if not visited[i]:
        bfs(i) # bfs() 호출
