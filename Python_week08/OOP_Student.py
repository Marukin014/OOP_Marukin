class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
        self.grade = {}
    def score(self,score):
        choice = input("รายชื่อวิชา : Mathematics Thai Science Social \n กรุณาเลือกวิชาที่ต้องการจะกรอกคะแนน : ")
        score = int(input('ใส่คะแนน : '))
        grades= self.grades(score)
        if choice == "Mathematics":
            self.grade["Mathematics"] = grades
        elif choice == "Thai":
            self.grade["Thai"] = grades
        elif choice == "Science":
            self.grade["Science"] = grades
        elif choice == "Social":
            self.grade["Social"] = grades   
    def grades(self,score):
        if score >= 80:
            return 4 
        elif score >= 70:
            return 3
        elif score >= 60:
            return 2 
        elif score >= 50:
            return 1 
        else:
            return 0

stu1 = Student("Mix",673001,19)
stu2 = Student("bob",673002,18)

stu1.score(70)
print(stu1.grade)
print(f"ชื่อนักศึกษา:{stu1.name} | รหัสประจำตัว:{stu1.id}")