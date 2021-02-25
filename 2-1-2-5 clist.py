### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 2 , Number 5 ###

class CList:
    class Node:
        def __init__(self, item, link): # 노드 생성자 , 항목과 앞뒤 노드 레퍼런스
            self.item = item
            self.next = link

    def __init__(self): # 원형연결리스트 생성자 , last와 항목 수(size)로 구성
        self.last = None
        self.size = 0

    def no_items(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        n = self.Node(item, None) # 새 노드 생성하여 n이 참조
        if self.is_empty():
            n.next = n            # 새 노드는 자신을 참조하고 last가 새 노드 참조
            self.last = n         # 새 노드는 자신을 참조하고 last가 새 노드 참조
        else:
            n.next = self.last.next # 새 노드는 첫 노드를 참조하고
            self.last.next = n      # last가 참조하는 노드와 새 노드 연결
        self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        x = self.last.next
        if self.size == 1:
            self.last = None        # empty 리스트 됨
        else:
            self.last.next = x.next # last가 참조하는 노드가 두 번째 노드를 연결
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            f = self.last.next
            p = f
            while p.next != f:  # 첫 노드가 다시 방문되면 루프 중단
                print(p.item, ' -> ', end='')
                p = p.next      # 노드들을 차례로 방문하기 위해
            print(p.item)

class EmptyError(Exception): # underflow 시 에러 처리
    pass
