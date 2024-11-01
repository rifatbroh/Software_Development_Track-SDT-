"""
    USE: 
    a class use as a template when we include methode,
    constructor, etc..
"""
class Student:
    def __init__(self, name, id, sec) -> None:
        self.name =  name
        self.id = id
        self.sec = sec
    
    def call(self):
        pass

stu_one = Student("rifat", 39, 'A')
stu_two = Student("prome", 30, 'A')

print(stu_one.name)
print(stu_two.id)
