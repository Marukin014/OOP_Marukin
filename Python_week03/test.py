a = 10
print(a/7)
print(a%7)

a = 10
b = 5
print(a == b)
print(a <= b)
print(a >= b)
print(a > b)
print(a < b)
print(a != b)

a = int(input('ใส่คะแนน: '))
if a > 5:
    print('สอบผ่าน')
elif a == 5:
    print('ปกติ')
else: 
    print('สอบตก')