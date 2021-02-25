### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 2 , Number 1 ###

class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item # 노드 생성자
            self.next = link # 항목과 다음 노드 레퍼런스

    def __init__(self):
        self.hand = None # 단순연결리스트 생성자
        self.size = 0    # head와 항목 수(size)로 구성

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():                        # empty인 경우
            self.head = self.Node(item, None)      # head가 새 노드 참조
        else:
            self.head = self.Node(item, self.head) # head가 새 노드 참조
        self.size += 1

    def insert_after(self, item, p):
        p.next = self.Node(item, p.next) # 새 노드가 p 다음 노드가 됨
        self.size += 1

    def delete_front(self):
        if self.is_empty(): # empty인 경우 에러 처리
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next # head가 둘째 노드를 참조
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty(): # empty인 경우 에러 처리
            raise EmptyError('Underflow')
        t = p.next
        p.next = t.next # p 다음 노드를 건너뛰어 연결
        self.size -= 1

    def search(self, target):
        p = self.head # head로부터 순차탐색
        for k in range(self.size):
            if target == p.item:
                return k # 탐색 성공
            p = p.next
        return None # 탐색 실패

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, ' -> ', end='')
            else:
                print(p.item)
            p = p.next # 노드들을 순차탐색

class EmptyError(Exception): # underflow시 에러 처리
    pass
