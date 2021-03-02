### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 7 , Number 1 ###

def selection_sort(a):
    for i in range(0, len(a)-1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > j: # 정렬 안된 부분에서 최솟값 찾기
                minimum = j
        a[i], a[minimum] = a[minimum], a[i] # 현재 원소와 최솟값 가진 원소 교환

a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬 전:\t', end='')
print(a)
selection_sort(a)
print('정렬 후:\t', end='')
print(a)
