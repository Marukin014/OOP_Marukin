class Cat:
#   pass #คือผ่านเฉยๆ
    def __init__(self,cat_name,cat_color):
        self.name = cat_name
        self.color = cat_color
    def cry(self):
        return self.name,"เมี้ยวๆ"
    def cry2(self):
        print(f"แมว {self.color} ชื่อ {self.cry()}")
mycat1 = Cat("ไอเทา","สีเทา")
mycat2 = Cat("ไอขาว","สีขาว")
#object = ชื่อclass
print(f"ชื่อแมว : {mycat1.name} | สีของแมว : {mycat1.color}")
print(f"ชื่อแมว : {mycat2.name} | สีของแมว : {mycat2.color}")
print(mycat1.cry())
print(mycat2.cry())
print(mycat1.cry2())
print(mycat2.cry2())