class Cat:
    def __init__(self,ชื่อ,อายุ,เพศ,สี):
        self.name = ชื่อ
        self.age = อายุ
        self.gender = เพศ
        self.color = สี
    def old(self):
        self.age +=1
cat1 = Cat(ชื่อ="สลิด",อายุ =1.5,เพศ = "ตัวผู้",สี = "เทา")
cat2 = Cat(ชื่อ="ไอขาว",อายุ =1 ,เพศ = "ตัวเมีย",สี = "ขาว")
cat2.age +=5
cat2.old()
print(cat1.name,cat2.name,cat1.age,cat2.age)
