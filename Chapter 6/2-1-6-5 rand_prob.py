### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 6 , Number 5 ###

import random # random 패키지 불러오기
class RandProbing:
    def __init__(self, size):  # 객체 생성자
        self.M = size          # 테이블 크기 M
        self.a = [None] * size # 해시테이블 a
        self.d = [None] * size # 데이터 저장용 d
        self.N = 0             # 항목 수

    def hash(self, key):
        return key % self.M # 나눗셈 해시 함수

    def put(self, size):                        # 삽입 연산
        initial_position = self.hash(key)       # 초기 위치
        i = initial_position
        random.seed(1000)                       # 난수 생성 초기값
        while True:
            if self.a[i] == None:
                if self.a[i] == None:           # 빈 곳 발견
                self.a[i] = key                 # key는 해시테이블에
                self.d[i] = data                # data는 리스트 d에 저장
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data                # data만 갱신
                return
            j = random.randint(1, 99)           # 난수 크기 범위 지정
            i = (initial_position + j) % self.M # 다음 원소 검사를 위해
            if self.N > self.M:
                break

    def get(self, key):
        initial_position = self.hash(key)                           # 초기 위치
        i = initial_position
        random.seed(1000)                                           # 저장할 때와 동일한 난수 생성 초기값
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]                                    # 탐색 성공
            i = (initial_position + random.randint(1, 99)) % self.M # 난수 크기 종일한 범위 지정
        return None
