### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 7 , Number 2 ###

def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1): # 현재 원소가 정렬된 부분에 십입될 곳을 찾아서
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j] # 현재 원소와 바로 앞의 원소 교환

a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬 전:\t', end='')
print(a)
insertion_sort(a)
print('정렬 후:\t', end='')
print(a)
