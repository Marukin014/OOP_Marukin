class Product:
    def __init__(self, name, price, quantity):
        """
        สร้าง Product
        :param name: ชื่อสินค้า
        :param price: ราคาสินค้า (float)
        :param quantity: จำนวนสินค้าในสต็อก (int)
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        """
        คำนวณราคารวมทั้งหมดของสินค้าในสต็อก
        :return: ราคาสุทธิ (float)
        """
        return self.price * self.quantity

    def add_stock(self, amount):
        """
        เพิ่มจำนวนสินค้าในสต็อก
        :param amount: จำนวนสินค้าที่ต้องการเพิ่ม (int)
        """
        if amount > 0:
            self.quantity += amount
        else:
            raise ValueError("จำนวนที่เพิ่มต้องมากกว่า 0")

    def remove_stock(self, amount):
        """
        ลดจำนวนสินค้าในสต็อก
        :param amount: จำนวนสินค้าที่ต้องการลด (int)
        """
        if 0 < amount <= self.quantity:
            self.quantity -= amount
        else:
            raise ValueError("จำนวนที่ลดต้องอยู่ในช่วงที่เหมาะสม")

    def __str__(self):
        """
        แสดงข้อมูลสินค้าในรูปแบบที่อ่านง่าย
        :return: ข้อมูลสินค้า (str)
        """
        return f"Product(name={self.name}, price={self.price:.2f}, quantity={self.quantity})"

# การใช้งาน
product = Product("Laptop", 25000.0, 10)
print(product)

product.add_stock(5)
print(f"หลังเพิ่มสต็อก: {product}")

product.remove_stock(3)
print(f"หลังลดสต็อก: {product}")

