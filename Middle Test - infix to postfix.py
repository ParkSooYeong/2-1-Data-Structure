# Sungkyul University - College of Engineering - Department of Information and Telecommunication Engineering - 20170910 Park Soo-young
# Data Structure Report : infix to postfix





def precedence(op):                 # 연산자 우선 순위 설정 함수 precedence 정의, 변수 op 정의
    
    if op == '*' or op == '/':      # 입력받은 연산자 중 '*'나 '/'가 있으면,
        return 2                    # 2 반환
    
    elif op == '+' or op == '-':    # 입력받은 연산자 중 '+'나 '-'가 있으면,
        return 1                    # 1 반환
    
    elif op == '(' or op == ')':    # 입력받은 연산자 중 '('나 ')'가 있으면,
        return 0                    # 0 반환
    
    else:                           # 위의 연산자 이외의 문자나 숫자가 있다면, 
        return -1                   # -1 반환



def infix_to_postfix():                                                     # 후위표기법 변환 함수 infix_to_postfix 정의
    
    calculation = input("후위표기법으로 변환할 수식을 입력해주세요. = ")    # 수식 입력 지시 메시지 출력 및 입력받은 수식을 변수 calculation에 저장

    index = " "                                                             # 구분을 위한 공백 변수 index 선언
    result = ""                                                             # 후위표기법으로 변환한 값들을 저장할 변수 result 선언
    stack = []                                                              # 스택(=리스트) 선언
 
    for i in calculation:                                                   # 스택의 응용 - 괄호 짝 맞추기 , 변수 i가 입력 식의 마지막 값을 읽을때까지 아래 코드 반복

        if i == '+' or i == '-' or i == '*' or i == '/':                    # i가 연산자를 읽으면,
            result += index                                                 # 구분을 위해 연산자 앞에 공백을 추가하고, 
            while stack and precedence(stack[-1]) >= precedence(i):         # 스택 맨 위의 문자의 우선 순위 이상의 연산자를 읽을 때까지, 
                  result += stack.pop()                                     # 값들을 pop하여서 result에 저장
            result += index                                                 # 구분을 위해 연산자 뒤에 공백을 추가하고, 
            stack.append(i)                                                 # i가 읽은 해당 연산자를 스택에 push
            continue                                                        # 아래 코드를 생략하고 다음 반복 시작

        elif i == '(':                                                      # i가 왼쪽 괄호를 읽으면,
            stack.append(i)                                                 # 스택에 push
            continue                                                        # 아래 코드를 생략하고 다음 반복 시작

        elif i == ')':                                                      # i가 오른쪽 괄호를 읽으면,
            result += index                                                 # 구분을 위해 읽을 값 앞에 공백을 추가하고,
            while stack[-1] != '(':                                         # 스택의 맨 위의 문자가 왼쪽 괄호가 되기 전까지, 
                result += stack.pop()                                       # 값들을 pop하여서 result에 저장
            result += index                                                 # 구분을 위해 읽은 값의 뒤에 공백을 추가하고,
            stack.pop()                                                     # 왼쪽 괄호는 pop하여 버림
            continue                                                        # 아래 코드를 생략하고 다음 반복 시작

        result += i                                                         # 위의 경우들이 아니라면, i가 읽은 값을 result에 저장

    while stack:                                                            # 스택을 비우기 위해
        result += index                                                     # 구분을 위해 공백을 추가하고, 
        result += stack.pop()                                               # 스택의 남은 값들을 pop하여서 result에 저장

    print("\n결과 = %s\n\n\n" % result)                                     # 후위표기법으로 변환한 결과를 출력



if __name__ == "__main__":                          # 메인 함수 시작

    while True:                                     # 편의성을 위한 무한루프
        print("종료하시려면 Ctrl+C를 입력하세요.")  # 무한루프 탈출 방법 메시지 출력
        infix_to_postfix()                          # 후위표기법 변환 함수 infix_to_postfix 호출
