### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 7 , Number 7 ###

def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high) # 피벗을 기준으로 분할
        qsort(a, low, pivot-1) # 앞/뒷부분 재귀호출
        qsort(a, pivot+1, high) # 앞/뒷부분 재귀호출

def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]: # a[i]가 피벗보다 작으면 i를 1증가
            i += 1
        while j > pivot and a[j] > a[pivot]: # a[j]가 피벗보다 작으면 j를 1감소
            j -= 1
        if j <= i: # 루프 중단
            break
        a[i], a[j] = a[j], a[i] # a[i]와 a[j] 교환
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot] # a[j]와 피벗 교환
    return j # 피벗 인덱스

a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬 전:\t', a)
qsort(a, 0, len(a)-1) # 퀵정렬 호출
print('정렬 후:\t', a)
