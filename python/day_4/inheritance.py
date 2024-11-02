class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running laptop: {self.brand}'
    
class laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'leraning python and practising'
    
class phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def phone_call(self, number, text):
        return f'Sending sms to {number} with: {text}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel
    # method
    def change_lens(self):
        pass

# inheritance
my_phone = phone('Iphone', 120000, 'silver', 'chaina', True)

print(my_phone.brand)
for i in my_phone(phone):
    print(i)
        