### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 1 , Number 2 ###

a = []              # 비어있는 리스트 a 선언
b = [None] * 10     # 크기가 10이고 각 원소가 None으로 초기화된 리스트
c = [0, 30, 40, 70] # 크기가 4이고 4개의 정수로 초기화된 리스트
print(c[0])         # 0 출력
print(c[-1])        # 70 출력
c.pop()             # 리스트 마지막 항목인 70 제거
c.pop(0)            # 리스트 첫 항목인 0 제거
c.append(100)       # 리스트 맨 뒤에 100 추가
print(len(c))       # 내장 함수인 len()은 리스트의 크기 리턴
