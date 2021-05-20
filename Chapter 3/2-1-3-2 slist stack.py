### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 3 , Number 2 ###

class Node:                         # Node 클래스
    def __init__(self, item, link): # Node 생성자 , 항목과 다음 노드 레퍼런스
        self.item = item
        self.next = link

def push(item):           # push 연산
    global top            # 전역 변수
    global size           # 전역 변수
    top = Node(item, top) # 새 노드 객체를 생성하여 연결리스트의 첫 노드로 삽입
    size += 1

def peek():             # peek 연산
    if size != 0:
        return top.item # top 항목만 리턴

def pop():              # pop 연산
    global top          # 전역 변수
    global size         # 전역 변수
    if size != 0:
        top_item = top.item
        top = top.next  # 연결리스트에서 top이 참조하던 노드 분리시킴
        size -= 1
        return top_item # 제거된 top 항목 리턴

def print_stack(): # 스택 출력
    print('top -> \t', end='')
    p = top
    while p:
        if p.next != None:
            print(p.item, ' -> ', end='')
        else:
            print(p.item, end='')
        p = p.next # 단순연결리스트(스택)의 항목을 차례로 방문
    print()

# 초기화
top = None
size = 0

push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후 : \t', end='')
print_stack()
print('top 항목 : ', end='')
print(peek())
push('pear')
print('배 push 후 : \t\t', end='')
print_stack()
pop()
push('grape')
print('pop(), 포도 push 후 : \t', end='')
print_stack()
