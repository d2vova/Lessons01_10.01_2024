class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record book: {self.record_book}"


class GroupOverflowError(Exception):
    def __init__(self, message="Неможливо додати більше 10 студентів у групу"):
        self.message = message
        super().__init__(self.message)


class Group:
    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupOverflowError
        self.students.append(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.students.remove(student_to_delete)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.students)
        return f"Number: {self.number}\n{all_students}"


st1 = Student("Male", 30, "Steve", "Jobs", 'AN142')
st2 = Student('Male', 32, 'Vova', 'Prykh', 'AN145')
st3 = Student('Male', 34, 'Sasha', 'Harl', 'AN145')
st4 = Student('male', 29, 'Kolya', 'Hreben', 'AN145')
st5 = Student('Female', 28, 'Olya', 'Karai', 'AN145')
st6 = Student('Female', 27, 'Liza', 'Desyatnik', 'AN145')
st7 = Student('Male', 28, 'Artem', 'Borodatyk', 'AN145')
st8 = Student('Male', 21, 'Oleh', 'Tolokonnikov', 'AN145')
st9 = Student('Female', 24, 'Valentyna', 'Tolokonn', 'AN145')
st10 = Student('Female', 23, 'Irina', 'Artamkina', 'AN145')
st11 = Student('Female', 29, 'Natasha', 'Karai', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

try:
    gr.add_student(st11)
except GroupOverflowError as e:
    print(e)


print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
