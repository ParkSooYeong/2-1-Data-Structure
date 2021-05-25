### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 8 , Number 3 ###

adj_list = [[3], [6, 10], [7, 11], [0, 6, 8], [13], [14], [1, 3, 8, 10, 11], [2, 11], [3, 6, 10, 12], [13], [1, 6, 8], [2, 6, 7], [8], [4, 9], [5]] # 그래프 인접리스트
N = len(adj_list)
CCList = []
visited = [False] * N # 정점 방문 여부 확인 용

def dfs(v):
    visited[v] = True
    cc.append(v) # 현재 연결성분에 정점 v 추가
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w) # 정점 v에 인접한 w로 dfs() 재귀호출

for i in range(N):
    if not visited[i]:
        cc = [] # 새로운 연결성분(cc)을 위한 초기화
        dfs(i) # dfs() 호출로 cc 만들기
        CCList.append(cc) # 완성된 cc를 연결성분 리스트에 추가

print('연결성분 리스트:')
print(CCList)
