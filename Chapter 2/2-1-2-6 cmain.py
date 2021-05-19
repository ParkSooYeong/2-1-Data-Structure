### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 2 , Number 6 ###

from clist import CList    # clist.py에서 CList를 import (2-1-2-5 clist.py를 clist.py로 이름 변경 필요)
if __name__ == '__main__': # 이 파이썬 파일(모듈)이 메인이면
    s = CList()            # 이중연결리스트 생성
    s.insert('pear')
    s.insert('cherry')
    s.insert('orange')
    s.insert('apple')
    s.print_list()
    print('s의 길이 = ', s.no_items())
    print('s의 첫 항목 : ', s.first())
    s.delete()
    print('첫 노드 삭제 후 : ', end='')
    s.print_list()
    print('s의 길이 = ', s.no_items())
    print('s의 첫 항목 : ', s.first())
    s.delete()
    print('첫 노드 삭제 후 : ', end='')
    s.print_list()
    s.delete()
    print('첫 노드 삭제 후 : ', end='')
    s.print_list()
    s.delete()
    print('첫 노드 삭제 후 : ', end='')
    s.print_list()
