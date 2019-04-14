class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        self.items[item_name] = quantity
        self.total = self.total + (price * quantity)
    
    def remove_item(self, item_name, quantity, price):
        current_quantity = self.items[item_name]
        if current_quantity < quantity:
            self.items.pop(item_name)
            self.total =  self.total - (price * current_quantity)
        else:
            new_quantity = current_quantity - quantity
            self.items[item_name] = new_quantity

            self.total = self.total - (price * quantity)
    
    def checkout(self, cash_paid): 
        if self.total > cash_paid:
            return 'Cash paid not enough'
        return (cash_paid - self.total)


class Shop(ShoppingCart):
    def __init__(self):
        self.quantity = 100
    
    def remove_item(self):
        self.quantity = self.quantity - 1