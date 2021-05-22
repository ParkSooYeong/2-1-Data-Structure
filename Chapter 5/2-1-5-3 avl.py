### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 5 , Number 3 ###

class Node:
    def __init__(self, key, value, height, left=None, right=None): # 노드 생성자 , key, value, 노드의 높이, 왼쪽, 오른쪽 자식노드 레퍼런스
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None # 트리 루트

    def height(self, n):
        if n == None:
            return 0
        return n.height # 노드 n의 높이 리턴

    def put(self, key, value): # 삽입 연산
    def balance(self, n): # 불균형 처리
    def bf(self, n): # bf 계산
    def rotate_right(self, n): # 우로 회전
    def rotate_left(self, n): # 좌로 회전
    # 삭제 및 삭제 관련 연산
    def delete(self, key): # 삭제 연산
    def delete_min(self): # 최솟값 연산
    def min(self): # 최솟값 찾기
