a = int(input("โปรดใส่ค่าที่ต้องการ: "))
for b in range(1,25,1):
    c = a * b
    d = c / 2
    if d % 2 != 0:
        print(f"{a} x {b} = {c}")