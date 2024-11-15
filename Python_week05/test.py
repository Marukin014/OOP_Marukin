a = [100,20,10,40,70,150]
#a.append(10)
#a.insert(1,50)
#a.remove(10) ลบ 10 
#a.pop(2) ลบลำดับที่ 2
while True:
    num = (int(input('หยอดเงินใส่กระปุก : ')))
    a.append(num)
    print(a)
    if num == 0:
        print(f"เงินเก็บทั้งหมด = {sum(a)}")
        break