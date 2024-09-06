items = {}

class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }
