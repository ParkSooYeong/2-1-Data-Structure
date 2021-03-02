### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 7 , Number 8 ###

def lsd_sort(a):
    WIDTH = 3 # 입력:3개의 문자로 된 스트링
    N = len(a)
    R = 128
    temp = [None] * N
    for d in reversed(range(WIDTH)): # 2, 1, 0 순으로
        count = [0] * (R+1)
        for i in range(N):
            count[ord(a[i][d])+1] += 1 # 빈도수 계산
        for j in range(1, R):
            count[j] += count[j-1] # temp에 저장할 시작 인덱스 계산
        for i in range(N):
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] += 1
            # d번째 문자를 기준으로 각 a[i]를 적절한 temp 원소로 복사
        for i in range(N):
            a[i] = temp[i]
        print('%d번째 문자:\t ' % d, end='')
        for x in a: print(x, ' ', end='')
        print()
a = ['ICN', 'SFO', 'LAX', 'FRA', 'SIN', 'ROM', 'HKG', 'TLV', 'SYD', 'MEX', 'LHR', 'NRT', 'JFK', 'PEK', 'BER', 'MOW']
print('정렬 전:\t\t', end='')
for x in a: print(x, ' ', end='')
print()
lsd_sort(a)
