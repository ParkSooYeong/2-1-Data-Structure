### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 5 , Number 2 ###

from bst import BST # (2-1-5-1 bst.py를 bst.py로 이름 변경 필요)
if __name__ == '__main__':
    t = BST() # 이진탐색트리 객체 생성
    # 12개의 항목 삽입
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')
    t.put(700, 'cherry')
    t.put(50, 'pear')
    t.put(350, 'lemon')
    t.put(10, 'plum')
    # 트리 순회 및 삭제 연산 수행
    print('전위순회"\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
    print('\n250: ', t.get(250))
    print('200 삭제 후:')
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
