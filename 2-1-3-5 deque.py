### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 3 , Number 5 ###

from collections import deque
dq = deque('data') # 새 데크 객체를 생성
for elem in dq:
    print(elem.upper(), end='')
print()
dq.append('r')     # 맨 뒤와 맨 앞에 항목 삽입
dq.appendleft('k') # 맨 뒤와 맨 앞에 항목 삽입
print(dq)
dq.pop()      # 맨 뒤와 맨 앞에 항목 삭제
dq.popleft()  # 맨 뒤와 맨 앞에 항목 삭제
print(dq[-1]) # 맨 뒤의 항목 출력
print('x' in dq)
dq.extend('structure')            # 맨 뒤와 맨 앞에 여러 항목 삽입
dq.extendleft(reversed('python')) # 맨 뒤와 맨 앞에 여러 항목 삽입
print(dq)
