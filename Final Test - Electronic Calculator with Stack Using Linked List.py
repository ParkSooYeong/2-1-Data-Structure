# Sungkyul University - College of Engineering - Department of Information and Telecommunication Engineering - 20170910 Park Soo-young
# Data Structure Final Examination Report : Electronic Calculator with Stack Using Linked List





import re   # 입력받은 식에서 숫자(특히 실수)와 연산자를 구분해내기 위한 '정규 표현식' 모듈 호출
            # 정규식 : 텍스트가 배열된 규칙을 뜻하는 패턴을 나타내는 텍스트



# 연결리스트로 구현한 스택

class Node:                         # Node 클래스
    def __init__(self, item, link): # Node 생성자 , 항목과 다음 노드 레퍼런스
        self.item = item
        self.next = link

def push(item):             # push 연산
    global top              # 전역변수 top
    global size             # 전역변수 size
    top = Node(item, top)   # 새 노드 객체를 생성하여 연결리스트의 첫 노드로 삽입
    size += 1

def pop():                  # pop 연산
    global top              # 전역변수 top
    global size             # 전역변수 size
    if size != 0:           
        top_item = top.item
        top = top.next      # 연결리스트에서 top이 참조하던 노드 분리
        size -= 1
        return top_item     # 제거된 top 항목 반환

top = None  # 초기화
size = 0    # 초기화



# 계산식 입력 함수 input_calculation 정의

def input_calculation():
    
    print("첫번째 식을 입력해주세요.")
    first = input("1 : ")                   # 첫번째 식을 입력받아 변수 first에 저장
    print("\n")
    print("두번째 식을 입력해주세요.")
    second = input("2 : ")                  # 두번째 식을 입력받아 변수 second에 저장
    print("\n")
    print("세번째 식을 입력해주세요.")
    third = input("3 : ")                   # 세번째 식을 입력받아 변수 third에 저장
    print("\n")
    print("네번째 식을 입력해주세요.")
    fourth = input("4 : ")                  # 네번째 식을 입력받아 변수 fourth에 저장
    print("\n")
    print("다섯번째 식을 입력해주세요.")
    fifth = input("5 : ")                   # 다섯번째 식을 입력받아 변수 fifth에 저장
    print("\n")

    push(first)
    push(second)
    push(third)
    push(fourth)
    push(fifth)
    
    # 입력한 첫번째 식부터 다섯번째 식을 차례대로 연결리스트로 구현한 스택에 push



# 계산식 표현 구분 함수 expression_delimetric 정의

def expression_delimetric(term):    # 매개변수 term 정의
    
    pattern = re.compile(   # 표현 구분 변수 pattern, 다음 문자열들을 패턴 객체로 컴파일
        r'(?:'              # (r = 패턴 명시) (괄호 = 그룹을 의미) (? = 조건문과 유사) 아래는 캡쳐하지 않는 그룹이라는 뜻
        r'(?<=[^\d\.])'     # 숫자나 소숫점이 아닌 문자가 왼쪽에 존재하고 (ex : PARK , 수영 등등)
        r'(?=\d)'           # 오른쪽에 숫자가 존재하는 지점 (ex : 박1 , 수2 , 영3 등등)
        r'|(?=[^\d\.])'     # 만약 숫자나 점 다음이라면, 그 다음은 숫자나 소수점이 아니어야 한다는 뜻 (ex : 4.. 등등)
        r')'                # 여기까지 설정한 패턴들은 캡쳐하지 않음.
        , re.MULTILINE)     # 패턴의 처음과 마지막이 위에 설정한 패턴들로 끝나야 매치된다는 뜻
    
    return [repeat for repeat in re.sub(pattern, ' ', term).split(' ') if repeat]

    # 반복문(변수 repeat 포함)을 사용하여 term에 들어온 입력식 중 패턴과 매치되는 텍스트를 공백으로 치환하여 반환하고 분할



# 후위표기법 변환 함수 infix_to_postfix 정의

def infix_to_postfix(infix):                    # 매개변수 infix 정의
    
    calculation = expression_delimetric(infix)  # 입력받은 중위표기식을 표현 구분하여 변수 calculation에 저장
    
    operator = ('*', '/', '+', '-', '(', ')')                           # 연산자 변수 operator 선언
    precedence = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0, ')' : 0} # 연산자 우선 순위 설정 변수 precedence 선언

    result = [] # 결과를 저장할 스택(=리스트) result 선언
    stack = []  # 계산식에 대한 작업을 진행할 스택(=리스트) stack 선언

    for i in calculation:       # 스택의 응용 - 괄호 짝 맞추기 , 변수 i가 입력 식의 마지막 값을 읽을때까지 아래 코드 반복
        
        if i not in operator:   # i가 읽은 것이 연산자가 아니면,
            result.append(i)    # result에 그것(숫자)을 push
            
        elif i == '(':          # i가 왼쪽 괄호를 읽으면,
            stack.append(i)     # stack에 push
            
        elif i == ')':                                  # i가 오른쪽 괄호를 읽으면,
            while stack != [] and stack[-1] != '(':     # stack의 맨 위의 문자가 왼쪽 괄호가 되기 전까지,
                result.append(stack.pop())              # stack의 값들을 pop하여서 result에 push
            stack.pop()                                 # 왼쪽 괄호는 stack에서 pop하여서 버림
            
        else:                                                               # i가 연산자를 읽으면,
            while stack != [] and precedence[stack[-1]] >= precedence[i]:   # stack의 맨 위의 문자의 우선 순위 이상의 연산자를 읽을 때까지,
                result.append(stack.pop())                                  # stack의 값들을 pop하여서 result에 push
            stack.append(i)                                                 # i가 읽은 해당 연산자를 stack에 push

    while stack:                    # i가 입력 식의 마지막 값을 읽었다면, stack을 비우기 위해
        result.append(stack.pop())  # stack의 남은 것들을 pop하여서 result에 push
    
    return result    # 후위표기법으로 변한한 결과인 result를 반환



# 후위표기식 계산 함수 run_calculation 정의

def run_calculation(postfix):   # 매개변수 postfix 정의
    
    operation = {               # 연산 변수 operation 선언
            '*' : lambda forward, backward: backward * forward,
            '/' : lambda forward, backward: backward / forward,
            '+' : lambda forward, backward: backward + forward,
            '-' : lambda forward, backward: backward - forward
            }

    # 익명함수(lambda)를 이용한 사칙연산 명시


    stack = []                                  # 계산 작업을 진행할 스택(=리스트) stack 선언

    for i in postfix:                           # 변수 i가 후위표기식의 마지막 값을 읽을때까지 아래 코드 반복
        
        if i not in operation:                  # i가 읽은 것이 연산자가 아니면,
            
            if '.' in i:                        # 그중에서도 i가 소수점(.)을 읽었다면,
                stack.append(float(i))          # stack에 그것(소수)을 실수형으로 push
                
            else:                               # i가 숫자를 읽으면,
                stack.append(int(i))            # stack에 그것(숫자)을 정수형으로 push
                
        else:                                               # i가 연산자를 읽으면,
            forward = stack.pop()                           # 현재 stack의 가장 위에 있는 값을 pop하여서 변수 forward에 저장
            backward = stack.pop()                          # stack의 그 다음에 있는 값을 pop하여서 변수 backward에 저장
            stack.append(operation[i](forward, backward))

            # 먼저 꺼낸 값이 연산자의 우변이 되어서 해당 연산자에 맞는 연산 진행 후, 결과를 stack에 push

            
    print("결과 : %s\n\n" % stack[-1])    # i가 후위표기식의 마지막 값을 읽었다면, stack에 남아있는 계산 결과를 출력



# 계산식 출력 함수 output_calculation 정의

def output_calculation(data):                         # 매개변수 data 정의
    
    return run_calculation(infix_to_postfix(data))

    # 입력된 중위표기식을 후위표기식으로 변환하고 변환된 후위표기식을 계산하여 그 결과값을 반환



def main():                 # 메인 함수 main 정의
    
    input_calculation()     # 계산식 입력 함수 input_calculation 호출
    
    for j in range(1,6):    # 반복문 사용 , 변수 j는 1부터 5까지 한 사이클마다 1씩 증가
        
        sequence = pop()    # 연결리스트로 구현한 스택에서 가장 위에 있는 값을 pop하여서 변수 sequence에 저장
        
        print(6-j, ":", infix_to_postfix(sequence))     # 후위표기법으로 변환 후, 입력 식의 원래 순서를 역순으로 출력
        
        output_calculation(sequence)    # 계산식 출력 함수 output_calculation 호출



if __name__ == "__main__":                              # 메인 함수 시작

    while True:                                         # 편의성을 위한 무한루프
        print("\n종료하시려면 Ctrl+C를 입력하세요.\n")    # 무한루프 탈출 방법 메시지 출력
        main()                                          # 메인 함수 main 호출
