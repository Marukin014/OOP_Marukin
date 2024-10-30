score = int(input('ใส่คะแนน : '))
if score > 100:
    print('error')

elif score >= 70:
    print('4')

elif score >= 70:
    print('3')
    
elif score >= 60:
    print('2')

elif score >= 50:
    print('1')

elif score < 50:
    print('คุณสอบตก')
    print('อยากสอบแก้ไหม')
    grade = str(input('พิมพ์ Y or N \n'))
    if grade == "Y":
        print("คุณขาดคะแนนอีก "+str(50-score)+" ถึงจะสอบผ่าน")
    elif grade == "N":
        print("คุณสอบแก้ตก")
else :
    print('ป้อนค่าไม่ถูกต้อง')

