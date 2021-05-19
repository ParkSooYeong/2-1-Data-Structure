### SKU CoE ITE - ParkSooYoung ###
### Grade 2 , Semester 1 , Chapter 1 , Number 1 ###

class Student:
    def __init__(self, name, id): # Student 객체 생성자
        # 인스턴스 변수
        self.name = name
        self.id = id
    def get_name(self): # 객체의 name을 리턴하는 메소드
        return self.name
    def get_id(self): # 객체의 id를 리턴하는 메소드
        return self.id

best = Student('Park', 101)
# best 학생의 name과 id 출력
print(best.get_name())
print(best.get_id())
