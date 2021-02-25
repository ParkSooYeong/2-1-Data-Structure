### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 2 , Number 2 ###

from slist import SList         # slist.py에서 SList를 import (2-1-2-1 slist.py를 slist.py로 이름 변경 필요)
if __name__ == '__main__':      # 이 파이썬 파일(모듈)이 메인이면
    s = SList()                 # 단순연결리스트 생성
    s.insert_front('orange')    # head -> orange
    s.insert_front('apple')     # apple -> orange -> cherry
    s.insert_after('cherry', s.head.next)
    s.insert_front('pear')
    s.print_list()              # pear -> apple -> orange -> cherry
    print('cherry는 %d번째' % s.search('cherry'))
    print('kiwi는', s.search('kiwi'))
    print('배 다음 노드 삭제 후 : \t\t', end='')
    s.delete_after(s.head)
    s.print_list()
    print('첫 노드 삭제 후 : \t\t', end='')
    s.delete_front()
    s.print_list()
    print('첫 노드로 망고, 딸기 삽입 후 : \t', end='')
    s.insert_front('mango')
    s.insert_front('strawberry')
    s.print_list()
    s.delete_after(s.head.next.next)
    print('오렌지 다음 노드 삭제 후 : \t', end='')
    s.print_list()
