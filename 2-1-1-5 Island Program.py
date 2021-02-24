### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 1 , Number 5 ###

class Node:
    def __init__(self, name, left=None, right=None): # 섬 생성자
        self.name = name
        self.left = left
        self.right = right

def map(): # 지도 만들기
    # 11개의 섬 만들기
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')
    n7 = Node('G')
    n8 = Node('H')
    n9 = Node('I')
    n10 = Node('J')
    n11 = Node('K')
    # 11개의 섬 교량을 잇기
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n5.left = n9
    n7.right = n10
    n9.right = n11
    return n1 # 시작 섬 리턴

def A_course(n): # A-코스
    if n != None:
        print(n.name, '-> ', end='') # 섬 n 방문
        A_course(n.left) # n의 왼쪽으로 진행
        A_course(n.right) # n의 오른쪽으로 진행

def B_course(n): # B-코스
    if n != None:
        B_course(n.left) # n의 왼쪽으로 진행
        print(n.name, '-> ', end='') # 섬 n 방문
        B_course(n.right) # n의 오른쪽으로 진행

def C_course(n): # C-코스
    if n != None:
        C_course(n.left) # n의 왼쪽으로 진행
        C_course(n.right) # n의 오른쪽으로 진행
        print(n.name, '-> ', end='') # 섬 n 방문

start = map() # 시작 섬을 n1으로
print('A-코스:\t', end='')
A_course(start)
print('\nB-코스:\t', end='')
B_course(start)
print('\nC-코스:\t', end='')
C_course(start)
