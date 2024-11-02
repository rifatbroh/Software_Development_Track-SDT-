class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        return super().make_sound()
    
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        return super().make_sound()
    
class Cow(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        return super().make_sound()
    
class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        return super().make_sound()
    

"""
    this is polymorphism and we create many form for this
"""

don = Cat('Real Don')
don.make_sound()

fake = Dog('fake dog')
fake.make_sound()

complex = Cow('complex cow')
complex.make_sound()

nature = Goat('nature goat')
nature.make_sound()