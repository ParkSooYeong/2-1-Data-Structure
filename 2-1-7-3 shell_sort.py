### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 7 , Number 3 ###

def shell_sort(a):
    h = 4 # 3x+1 간격: 1, 4, 13, 40, 121, ... 중에서 4와 1만 사용
    while h >= 1:
        for i in range(h, len(a)): # h-정렬 수행
            j = i
            while j >= h and a[j] < a[j-h]: # 각 그룹에 대해 삽입정렬 수행
                a[j], a[j-h] = a[j-h], a[j] # 각 그룹에 대해 삽입정렬 수행
                j -= h                      # 각 그룹에 대해 삽입정렬 수행
        h //= 3 # 다음 h 값 계산
a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬 전:\t', end='')
print(a)
shell_sort(a)
print('정렬 후:\t', end='')
print(a)
