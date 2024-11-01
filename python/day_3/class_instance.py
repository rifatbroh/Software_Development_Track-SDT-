"""
    same method and process but define as single single
"""
class Shop:
    #cart = []
    def __init__(self, buyer) -> None:
        self.buyer = buyer
        # for single person
        self.cart = []

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