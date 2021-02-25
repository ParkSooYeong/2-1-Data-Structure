### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 2 , Number 3 ###

class DList:
    class Node:
        def __init__(self, item, prev, link): # 노드 생성자 , 항목과 앞뒤 노드 레퍼런스
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self): # 이중연결리스트 생성자 , head와 tail, 항목 수(size)로 구성
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p) # 새 노드 생성하여 n이 참조
        p.prev = n                # 새 노드와 앞뒤 노드 연결
        t.next = n                # 새 노드와 앞뒤 노드 연결
        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p, t) # 새 노드 생성하여 n이 참조
        t.prev = n    # 새 노드와 앞뒤 노드 연결
        p.next = n    # 새 노드와 앞뒤 노드 연결
        self.size += 1

    def delete(self, x):
        f = x.prev
        r = x.next
        f.next = r # x를 건너 뛰고 x의 앞뒤 노드를 직접 연결
        r.prev = f # x를 건너 뛰고 x의 앞뒤 노드를 직접 연결
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p = p.next # 노드들을 차례로 방문하기 위해

class EmptyError(Exception): # underflow 시 에러 처리
    pass
