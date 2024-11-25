class Gun:
    def __init__(self,name,ammo,hp):
        self.name = name
        self.ammo = ammo
        self.hp = hp
    def add_ammo(self,ammo):
        self.ammo += ammo
    def fire_ammo(self):
        if self.ammo > 0:
            self.ammo -=1
        else:
            print("กระสุนหมด")
    def fire_gun(self,enemy):
        self.ammo -= 1
        enemy.hp -= 4

gun1 = Gun("M4",20,10)
gun2 = Gun("M4",20,10)
gun1.fire_gun(gun2)
gun2.fire_gun(gun1)
gun1.fire_gun(gun2)
print("คนที่ 1")
print(gun1.ammo)
print(gun1.hp)
print("-------------")
print("คนที่ 2")
print(gun2.ammo)
print(gun2.hp)
