### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 1 , Number 3 ###

import random # random 모듈 불러오기
import time # time 모듈 불러오기
random.seed(time.time()) # 난수 생성을 위한 초기값을 현재 시각으로
a = []
for i in range(100):
    a.append(random.randint(1, 1000)) # 1과 1000 사이의 난수 1개를 생성하여 a에 추가

start_time = time.time() # 현재 시각을 시작 시간으로 지정

# 수행시간을 측정할 부분

print("--- %s seconds ---" % (time.time() - start_time)) # 현재 시각(종료 시각) - 시작 시간
