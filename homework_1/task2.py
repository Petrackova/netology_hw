class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades_lesson:
                lector.grades_lesson[course] += [grade]
            else:
                lector.grades_lesson[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lesson = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Иван', 'Иванов', 'm')
student_2 = Student('Петр', 'Сидоров', 'm')

student_1.grades['Java'] = [4, 10, 8, 3, 7]
student_2.grades['Python'] = [10, 8, 8, 6, 3]

lector_1 = Lecturer('Владимир', 'Епифанцев')

reviewer_1 = Reviewer('Сергей', 'Нечаев')

lector_1.courses_attached += (['Java'])
lector_1.courses_attached += (['Python'])

reviewer_1.courses_attached += (['Python'])
reviewer_1.courses_attached += (['Java'])

student_1.courses_in_progress += (['Python'])
student_2.courses_in_progress += (['Java'])

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Java', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Java', 3)


student_1.rate_lecture(lector_1, 'Python', 4)
student_1.rate_lecture(lector_1, 'Java', 6)
student_2.rate_lecture(lector_1, 'Python', 7)
student_2.rate_lecture(lector_1, 'Java', 10)

print(student_1.grades)
print(student_2.grades)
print(lector_1.grades_lesson)