### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 5 , Number 1 ###

class Node:
    def __init__(self, key, value, left=None, right=None): # 노드 생성자 , 키 항목과 왼쪽, 오른쪽자식 레퍼런스
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self): # 트리 생성자
        self.root = None # 트리 루트

    # 탐색, 삽입, 삭제 연산 min()과 delete_min()은 삭제 연산에서 사용됨
    def get(self, key): # 탐색 연산
    
    def put(self, key, value): # 삽입 연산
    
    def min(self): # 최솟값 가진 노드 찾기

    def delete_min(self): # 최솟값 삭제

    def delete(self, key): # 삭제 연산
