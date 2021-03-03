### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 9 , Number 3 ###

def min_run_len(N):
    r = 0
    while N >= 64:
        r = r | (N & 1)
        N >>= 1
    return N + r
