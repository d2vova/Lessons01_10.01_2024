from student import Student


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
