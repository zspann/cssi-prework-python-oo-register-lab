class CashRegister:
    def __init__(self, discount=0):
        self.total=0
        self.discount=discount
        self.items=[]


    def add_item(self, item, price, quant=1):
        self.total += price * quant
        for i in range(quant):
            self.items.append(item)
        self.last_transaction_price = price * quant
        self.last_quant = quant

    def apply_discount(self):
        if self.discount !=0:
            self.total = (self.total * (100.0 - self.discount)/100)
            return "After the discount, the total comes to ${:.2f}.".format(self.total)
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        self.total = self.total - self.last_transaction_price
        del self.items[len(self.items)-self.last_quant:len(self.items)]
