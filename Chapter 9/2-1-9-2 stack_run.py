### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 9 , Number 2 ###

while stack_size > 1:
    top = stack_size-1
    if top>2 and run[top-2]<=run[top-1]+run[top]: # 조건(1)이 위배되면
        if run[top-2]<run[top]:
            merge(top-2, top-1)
        else:
            merge(top-1, top)
    elif run[top-1]<=run[top]: # 조건(2)가 위배되면
        merge(top-1, top)
    else: # 두 조건 모두 만족
        break
