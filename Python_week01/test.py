class Studen:
    def __init__(self,name,scoure):
        self.name = name 
        self.scoure = scoure
    def showgrade(self):
        score = self.score
        if score >= 50:
            print(f"คุณ{self.name} ผ่านการสอบ")
        else :
            print(f"คุณ{self.name} ไม่ผ่านการสอบ")
    def showscore(self):
        print(f"คุณ {self.name} ได้คะแนน {self.score}")

studen1 = Studen("สมชาย",70)
studen2 = Studen("สมหญิง",49)        

studen1.showgrade()
studen2.showgrade()
studen2.showgrade()