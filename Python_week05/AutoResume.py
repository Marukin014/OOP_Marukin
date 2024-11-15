numbers = {}
default = int(input("ต้องการป้อนทั้งหมดกี่ตัว"))
for i in range(1,default+1):
    print(f'จำนวนคนที่ {i}')
    numbers['nickname'] = (str(input('กรุณากรอกชื่อเล่น : ')))
    numbers['stdid'] = (int(input(f'กรุณากรอกเลขที่  : ')))
    numbers['hobby'] = (str(input('กรุณากรอกงานอดิเรก : ')))
    numbers['color'] = (str(input('กรุณากรอกสีที่ชอบ : ')))
    print(f"ข้อมูลคนที่ {str(i)}\n{numbers}")
