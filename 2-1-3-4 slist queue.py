### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 3 , Number 4 ###

class Node:
    def __init__(self, item, n): # Node 생성자 , 항목과 다음 노드 레퍼런스
        self.item = item
        self.next = n

def add(item):                  # 삽입 연산
    global size                 # 전역 변수
    global front                # 전역 변수
    global rear                 # 전역 변수
    new_node = Node(item, None) # 새 노드 객체를 생성
    if size == 0:
        front = new_node        # 연결리스트의 맨 뒤에 삽입
    else:
        rear.next = new_node    # 연결리스트의 맨 뒤에 삽입
    rear = new_node
    size += 1

def remove():              # 삭제 연산
    global size            # 전역 변수
    global front           # 전역 변수
    global rear            # 전역 변수
    if size != 0:
        fitem = front.item
        front = front.next # 연결리스트에서 front가 참조하던 노드 분리시킴
        size -= 1
        if size == 0:
            rear = None
        return fitem       # 제거된 맨 앞의 항목 리턴

def print_q(): # 큐 출력
    p = front
    print('front : ', end='')
    while p:
        if p.next != None:
            print(p.item, '-> ', end='') # 단순연결리스트(스택)의 항목을 차례로 출력
        else:
            print(p.item, end='')
        p = p.next
    print(' : rear')

# 초기화
front = None
rear = None
size = 0
add('apple')
add('orange')
add('cherry')
add('pear')
print('사과, 오렌지, 체리, 배 삽입 후 : \t', end='')
print_q()
remove()
print('remove한 후 : \t\t', end='')
print_q()
remove()
print('remove한 후 : \t\t', end='')
print_q()
add('grape')
print('포도 삽입 후 : \t\t', end='')
print_q()
