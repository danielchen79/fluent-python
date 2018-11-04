'''
>>> apples = LineItem("Apple", 10, 1.9)
>>> apples.subtotal()
19.0
'''


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    import doctest
    doctest.testmod()
