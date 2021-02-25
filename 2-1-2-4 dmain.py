### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 2 , Number 4 ###

from dlist import DList    # dlist.py에서 DList를 import (2-1-2-3 dlist.py를 dlist.py로 이름 변경 필요)
if __name__ == '__main__': # 이 파이썬 파일(모듈)이 메인이면
    s = DList()            # 이중연결리스트 생성
    s.insert_after(s.head, 'apple')
    s.insert_before(s.tail, 'orange')
    s.insert_before(s.tail, 'cherry')
    s.insert_after(s.head.next, 'pear')
    s.print_list()
    print('마지막 노드 삭제 후 : \t', end='')
    s.delete(s.tail.prev)
    s.print_list()
    print('맨 끝에 포도 삽입 후 : \t', end='')
    s.insert_before(s.tail, 'grape')
    s.print_list()
    print('첫 노드 삭제 후 : \t', end='')
    s.delete(s.head.next)
    s.print_list()
    print('첫 노드 삭제 후 : \t', end='')
    s.delete(s.head.next)
    s.print_list()
    print('첫 노드 삭제 후 : \t', end='')
    s.delete(s.head.next)
    s.print_list()
    print('첫 노드 삭제 후 : \t', end='')
    s.delete(s.head.next)
    s.print_list()
