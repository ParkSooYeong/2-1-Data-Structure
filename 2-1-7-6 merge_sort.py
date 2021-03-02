### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 7 , Number 6 ###

def merge(a, b, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high+1): # a의 앞/뒷부분 합병하여 b에 저장
        if i > mid: 
            b[k] = a[j] # a의 앞부분이 먼저 소진되어 뒷부분을 b로 복사
            j += 1
        elif j > high:
            b[k] = a[i] # a의 앞부분이 먼저 소진되어 앞부분을 b로 복사
            i += 1
        elif a[j] < a[i]:
            b[k] = a[j] # a[j]가 승자
            j += 1
        else:
            b[k] = a[i] # a[i]가 승자
            i += 1
    for k in range(low, high+1):
        a[k] = b[k] # b를 a로 복사

def merge_sort(a, b, low, high):
    if high <= low:
        return
    mid = low + (high - low) // 2 # 중간 인덱스
    merge_sort(a, b, low, mid) # 앞/뒷부분 재귀호출
    merge_sort(a, b, mid + 1, high) # 앞/뒷부분 재귀호출
    merge(a, b, low, mid, high) # 정렬된 앞/뒷부분 합병

a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
b = [None] * len(a) # 보조 리스트
print('정렬 전:\t', end='')
print(a)
merge_sort(a, b, 0, len(a)-1) # 합병정렬 호출
print('정렬 후:\t', end='')
print(a)
