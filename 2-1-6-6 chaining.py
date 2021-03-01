### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 6 , Number 6 ###

class Chaining:
    class Node:
        def __init__(self, key, data, link): # 노드 객체 생성자 key, data, next
            self.key = key
            self.data = data
            self.next = link

    def __init__(self, size): # Chaining 객체 생성자 , 해시테이블 a
        self.M = size
        self.a = [None] * size

    def hash(self, key):
        return key % self.M # 나눗셈 해시함수

    def put(self, key, data):                       # 삽입 연산
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:
                p.data = data                       # key가 이미 있으면 data만 갱신
                return
            p = p.next
        self.a[i] = self.Node(key, data, self.a[i]) # 새 노드 생성 , 단순연결리스트 맨 앞에 삽입

    def get(self, key):      # 탐색 연산
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key: # 탐색 성공
                return p.data
            p = p.next
        return None          # 탐색 실패

    def print_table(self): # 테이블 출력
        for i in range(self.M):
            print('%2d' % (i), end='')
            p = self.a[i]
            while p != None:
                print('-->[', p.key, ',', p.data, ']', end='')
                p = p.next;
            print()
