class Bank:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount >= 100:
            self.__balance += amount
        else:
            print('ใส่ยอดเงิน 100 บาทขึ้นไป')

    def withdraw(self,amount):
        if amount >= 100:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print('ยอดเงินไม่เพียงพอ')
        else:
            print('ใส่ยอดเงิน 100 บาทขึ้นไป')
    
    def check(self):
        return self.__balance

id1 = Bank(1,"Mix",5000)
id1.__balance += 300
id1.withdraw(1000)
print(f'เงินของ {id1.name} มีอยู่ {id1.check()} บาท')
