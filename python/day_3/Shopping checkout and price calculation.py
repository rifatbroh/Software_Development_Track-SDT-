"""
    shopping checkout and price calculation
"""
class Shopping:
    def __init__(self, name) -> None:
        self.name = name
        self.cart = []

    def add_to_cart(self, item,price, quantity):
        product = {'item': item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)

    def remove_item(self, item):
        pass
    def checkout(self, amount):
        # basic calculation
        total = 0
        for item in self.cart:
            print(item)
            total += item['price'] * item['quantity']
            print("total price is : ", total)

            if amount < total:
                print(f'please provide {total-amount} more')
            else:
                change = amount - total
                print(f'Here is your items and extra money: {change}')


# define objec and pass data in class

shopno = Shopping("Rifat Hossain")
shopno.add_to_cart('alu', 65, 5)
shopno.add_to_cart('dim', 10, 12)
shopno.add_to_cart('rice', 90, 5)

print(shopno.cart)
shopno.checkout(1000)