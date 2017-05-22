class CashRegister():
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, item, price, quantity = 1):
        self.last_price = (price * quantity)
        self.total += self.last_price
        self.item_quantity = quantity
        for i in range(quantity):
            self.items.append(item)

    def apply_discount(self):
        if self.discount > 0:
            self.discount = 1 - (self.discount/100)
            self.total = self.discount * self.total
            return "After the discount, the total comes to $" + str(self.total) + "."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        self.total = self.total - self.last_price
        for i in range(self.item_quantity):
            self.items.pop()
