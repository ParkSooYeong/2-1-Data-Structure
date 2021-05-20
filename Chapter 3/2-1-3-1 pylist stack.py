### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 3 , Number 1 ###

def push(item):        # 삽입 연산
    stack.append(item) # push() = append() , 리스트의 맨 뒤에 item 추가

def peek():              # top 항목 접근
    if len(stack) != 0:
        return stack[-1] # top 항목 = 리스트의 맨 뒤 항목 리턴

def pop():                   # 삭제 연산
    if len(stack) != 0:
        item = stack.pop(-1) # pop() , 리스트의 맨 뒤에 있는 항목 제거
        return item

stack = [] # 리스트 선언
push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후 : \t', end='')
print(stack, '\t <- top')
print('top 항목 : ', end='')
print(peek())
push('pear')
print('배 push 후 : \t\t', end='')
print(stack, '\t <- top')
pop()
push('grape')
print('pop(), 포도 push 후 : \t', end='')
print(stack, '\t <- top')
