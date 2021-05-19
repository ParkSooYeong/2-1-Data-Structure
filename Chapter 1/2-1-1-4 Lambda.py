### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 1 , Number 4 ###

a = [1, 3, 4, 7, 10, 13, 0, 14]
even = list(filter(lambda x: (x%2 == 0), a)) # a에서 짝수만 선택하여 리스트로 리턴
print(even)
ten_times = list(map(lambda x: x * 10, a)) # a의 각 숫자를 10배로 만들어 리스트로 리턴
print(ten_times)

b = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]]
b.sort(key = lambda x: x[2]) # b의 각 원소(리스트)의 마지막 숫자를 기준으로 정렬
print(b)
