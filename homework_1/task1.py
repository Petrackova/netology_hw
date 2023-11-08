class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


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
student_3 = Student('Ольга', 'Иванова', 'f')
student_4 = Student('Инга', 'Скворцова', 'f')
student_1.grades['Java'] = [4, 10, 8, 3, 7]
student_2.grades['Python'] = [10, 8, 8, 6, 3]

mentor_1 = Mentor('Сергей', 'Харланов')
mentor_2 = Mentor('Виктор', 'Охлобыстин')

lector_1 = Lecturer('Владимир', 'Епифанцев')
lector_2 = Lecturer('Михаил', 'Познер')

reviewer_1 = Reviewer('Сергей', 'Нечаев')
reviewer_2 = Reviewer('Олег', 'Монгол')

lector_1.courses_attached += (['Java'])
lector_1.courses_attached += (['Python'])

reviewer_1.courses_attached += (['Python'])
reviewer_1.courses_attached += (['Java'])

student_1.courses_attached += (['Python'])
student_2.courses_attached += (['Java'])

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Java', 10)
reviewer_1.rate_hw(student_2, 'Java', 1)
reviewer_1.rate_hw(student_2, 'Java', 4)

print(f'Студент: {student_1.surname} {student_1.name}')
print(f'Оценки за курс: {student_1.grades}')
print(f'Студент: {student_2.surname} {student_2.name}')
print(f'Оценки за курс: {student_2.grades}')

print(f'Контроллер: {reviewer_1.surname} {reviewer_1.name}')
print(f'Курсы: {reviewer_1.courses_attached}')

print(f'Ментор: {mentor_1.surname} {mentor_1.name}')
print(f'Ментор: {mentor_2.surname} {mentor_2.name}')

print(f'Лектор: {lector_1.surname} {lector_1.name}')
print(f'Курсы: {lector_1.courses_attached}')
