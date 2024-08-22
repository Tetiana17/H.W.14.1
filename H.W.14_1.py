class MaxStudents(Exception):
    def __init__(self, message="max students"):
        self.message = message
        super().__init__(self.message)
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Gender: {self.gender}, Age: {self.age}, Name: {self.first_name} {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age,first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.max_students = 10

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise MaxStudents()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group) if self.group else 'No student in the group.'
        return f'Number: {self.number}\\n {all_students}'
stud = [
    Student("Male", 30, "Steve", "Jobs", "AN1"),
    Student("Female", 22, "Jane", "Doe", "AN2"),
    Student("Male", 25, "John", "Smith", "AN3"),
    Student("Female", 28, "Alice", "Johnson", "AN4"),
    Student("Male", 32, "Bob", "Brown", "AN5"),
    Student("Female", 27, "Carol", "Davis", "AN6"),
    Student("Male", 29, "Dave", "Wilson", "AN7"),
    Student("Female", 24, "Eve", "Taylor", "AN8"),
    Student("Male", 26, "Frank", "Miller", "AN9"),
    Student("Female", 31, "Grace", "Moore", "AN10"),
    Student("Male", 27, "Grag", "Moor", "AN11"),
]

gr = Group("PD1")


for i in stud:
    try:
        gr.add_student(i)
    except MaxStudents as e:
        print(e)  # Only one student

print(gr)
