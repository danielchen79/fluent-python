'''
>>> coconuts = LineItem('Brazilian coconut', 20, 17.95)
>>> coconuts.weight, coconuts.price
(20, 17.95)
>>> getattr(coconuts, '_Quantity#0'), getattr(coconuts, '_Quantity#1')
(20, 17.95)
'''

import model_v4c as model

class LineItem:
    weight = model.Quantity("weight")
    price = model.Quantity("price")

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == '__main__':
    import doctest
    doctest.testmod()
