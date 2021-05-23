### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 6 , Number 2 ###

from linear_prob import LinearProbing
if __name__ == '__main__':
    t = LinearProbing(13) # 해시테이블 크기가 13인 객체 생성
    # 8개의 항목 삽입
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon')
    # 탐색과 테이블 출력
    print('탐색 결과:')
    print('50의 data = ', t.get(50))
    print('63의 data = ', t. get(63))
    print('해시테이블:')
    t.print_table()
