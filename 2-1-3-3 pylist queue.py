### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 3 , Number 3 ###

def add(item):     # 삽입 연산
    q.append(item) # 맨뒤에 새 항목 삽입

def remove():          # 삭제 연산
    if len(q) != 0:
        item = q.pop() # 맨 앞의 항목 삭제
        return item

def print_q(): # 큐 출력
    print('front -> ', end='')
    for i in range(len(q)):
        print('{!s:<8}'.format(q[i]), end='') # 맨 앞부터 항목들을 차례로 출력
    print(' <- rear')

q = [] # 리스트 선언
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
