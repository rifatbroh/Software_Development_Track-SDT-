class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500: 
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

    def __repr__(self) -> str:
        result = f'welcome to {self.name}\n'
        result += '--------OUR Teachers--------\n'
        for teacher in self.teachers:
            result += str(teacher) + '\n'
        result += '--------OUR STUDENTS--------\n'
        for student in self.students:
            result += str(student) + '\n'
        return result + 'All Done for now'

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f'Teacher: {self.name}, Subject: {self.subject}, ID: {self.id}'

class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self):
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id}'

# Example usage
school = School("Phitron")
school.add_teacher("Tom Cruise", "Algo")
school.add_teacher("Leonardo DiCaprio", "DS")
school.add_teacher("Angelina Jolie", "Database")

school.enroll("Alia", 5200)
school.enroll("Rani", 8000)
school.enroll("Aishwarya", 7000)
school.enroll("Vaijaan", 90000)

print(school)
