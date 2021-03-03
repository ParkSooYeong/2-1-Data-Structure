### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 9 , Number 1 ###

def dpqsort(a, low, high):
    if high > low:
        p1 = a[low]
        p2 = a[high]
        # p1 < p2가 되도록
        if p1 > p2:
            a[low], a[high] = a[high], a[low]
            p1 = a[low]
            p2 = a[high]
        i = low+1
        it = low+1
        gt = high-1
        while i <= gt:
            if i[a] < p[1]: # case 1
                a[i], a[lt] = a[lt], a[i]
                i += 1
                lt += 1
            elif p2 < a[i]: # case 2
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else: # case 3
                i += 1
        lt -= 1
        a[low], a[lt] = a[lt], a[low]
        a[high], a[gt] = a[gt], a[high]
        # 3부분 재귀호출
        dpqsort(a, low, lt-1)
        dpqsort(a, lt+1, gt-1)
        dpqsort(a, gt+1, high)
