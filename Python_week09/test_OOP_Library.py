class Library:
    def __init__(self):
        self.namebook = []
    def add_book(self):
        while True:
            choice = input("พิมพ์ AddBook เพื่อเพิ่มและพิมพ์ Exit เพื่ออก : ")
            if choice == 'AddBook':
                     bookname = str(input('ใส่ชื่อหนังสือ : '))
                     self.namebook.append(bookname)
            elif choice == 'Exit':
                 break
    def show_books(self):
        print("รายชื่อหนังสือในห้องสมุดทั้งหมด:")
        for show_book in self.namebook:
            print(show_book)
    def find_book(self):
        bookname = str(input('ค้นหาชื่อหนังสือที่ต้องการจะหา:'))
        for i in self.namebook:
            if bookname == i:
                print(i)
user1 = Library()
user1.add_book()
user1.show_books()
user1.find_book()
print(user1.namebook)