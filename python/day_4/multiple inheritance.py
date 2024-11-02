class Family:
    def __init__(self, address) -> None:
        self.address = address

class School:
    def __init__(self, id, name, level) -> None:
        self.id = id
        self.name = name
        self.level = level

class Sports:
    def __init__(self, game, venue) -> None:
        self.game = game
        self.venue = venue

# multiple begins here
class Student(Family, School, Sports):
    def __init__(self, address, id, name, level, game, venue) -> None:
        Family.__init__(self, address)
        School.__init__(self, id, name, level)
        Sports.__init__(self, game, venue)
