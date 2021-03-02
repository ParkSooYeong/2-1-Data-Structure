### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 7 , Number 5 ###

import heapq
a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬 전:\t', a)

heapq.heapify(a) # 최소힙 만들기
print('힙:\t', a)

s = []
while a:
    s.append(heapq.heappop(a)) # 리스트 a의 가장 작은 항목을 삭제하여 리스트 s의 맨 뒤에 추가
print('정렬 후:\t', s)
