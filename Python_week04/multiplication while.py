a = int(input("โปรดใส่ค่าที่ต้องการ: "))
b = 1
while b <= 24:
    c = a * b
    d = c / 2
    if d % 2 != 0:
        print(f"{a} x {b} = {c}")
    b += 1