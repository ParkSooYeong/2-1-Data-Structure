### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 5 , Number 4 ###

from avl import AVL # (2-1-5-3 avl.py를 avl.py로 이름 변경 필요)
if __name__ == '__main__':
    t = AVL() # AVL 트리 객체 생성
    # 10개의 항목 삽입
    t.put(75, 'apple')
    t.put(80, 'grape')
    t.put(85, 'lime')
    t.put(20, 'mango')
    t.put(10, 'strawberry')
    t.put(50, 'banana')
    t.put(30, 'cherry')
    t.put(40, 'watermelon')
    t.put(70, 'melon')
    t.put(90, 'plum')
    # 트리 순회 및 삭제 연산 수행
    print('전위순회"\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
    print('\n75와 85 삭제 후 :')
    t.delete(75)
    t.delete(85)
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
