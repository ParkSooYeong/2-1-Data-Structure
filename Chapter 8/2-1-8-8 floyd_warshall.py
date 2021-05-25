### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 8 , Number 8 ###

import sys # sys.maxsize(최댓값) 사용 위해
N = 5
INF = sys.maxsize
D = [[0, 4, 2, 5, INF], [INF, 0, 1, INF, 4], [1, 3, 0, 1, 2], [-2, INF, INF, 0, 2], [INF, -3, 3, 1, 0]] # 입력 그래프의 인접행렬

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k]+D[k][i]) # 간선완화

for i in range(N): # 최단거리 출력
    for j in range(N):
        print('%3d' % D[i][j], end='')
    print()
