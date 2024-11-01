"""
    define a list like global and add
    something in list,
    after added for difference person
    the ultimate list is added all of
    them and so on ...
"""
class Shop:
    cart = []
    def __init__(self, buyer) -> None:
        self.buyer = buyer

    def add_to_cart(self, goods):
        self.cart.append(goods)

# various type of customer
razil = Shop("Razil")
razil.add_to_cart("Shoes")
razil.add_to_cart("bag")
print(razil.buyer)
print("After shopping: ", razil.cart)

rayhan = Shop("Rayhan")
rayhan.add_to_cart("sunglass")
rayhan.add_to_cart("joggars")
print(rayhan.buyer)
print("After shopping: ", rayhan.cart)

moneem = Shop("Moneem")
moneem.add_to_cart("books")
moneem.add_to_cart("pencil")
print(moneem.buyer)
print("After shopping: ", moneem.cart)