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

    def summ_s(self):
        summ = 0
        count = 0
        for i in self.grades.values():
            for j in i:
                summ += j
                count += 1
        return summ / count

    def __str__(self):
        return f'Имя студента: {self.name}\nФамилия студента: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(self.summ_s(), 1)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        if self.summ_s() > other.summ_s():
            return f'{self.surname} {self.name}'
        else:
            return f'{other.surname} {other.name}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lesson = {}

    def summ_s(self):
        summ = 0
        count = 0
        for i in self.grades_lesson.values():
            for j in i:
                summ += j
                count += 1
        return summ / count

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        if self.summ_s() > other.summ_s():
            return f'{self.surname} {self.name}'
        else:
            return f'{other.surname} {other.name}'

    def __str__(self):
        return f'Имя лектора: {self.name}\nФамилия лектора: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(self.summ_s(), 1)}\n'
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

    def __str__(self):
        return f'Имя проверяющего: {self.name}\nФамилия проверяющего: {self.surname}\n'


student_1 = Student('Иван', 'Иванов', 'm')
student_2 = Student('Петр', 'Сидоров', 'm')

mentor_1 = Mentor('Сергей', 'Харланов')
mentor_2 = Mentor('Виктор', 'Охлобыстин')

lector_1 = Lecturer('Владимир', 'Епифанцев')
lector_2 = Lecturer('Михаил', 'Познер')

reviewer_1 = Reviewer('Сергей', 'Нечаев')
reviewer_2 = Reviewer('Олег', 'Монгол')

lector_1.courses_attached += (['Java'])
lector_1.courses_attached += (['Python'])
lector_2.courses_attached += (['Java'])
lector_2.courses_attached += (['Python'])

reviewer_1.courses_attached += (['Python'])
reviewer_2.courses_attached += (['Java'])

student_1.finished_courses += ['Введение в программирование']
student_1.grades['Введение в программирование'] = [5, 6, 5, 7, 7]
student_2.finished_courses += ['Введение в программирование']
student_2.grades['Введение в программирование'] = [3, 3, 10, 8, 7]

student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Java', 5)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 3)

student_1.rate_lecture(lector_1, 'Python', 7)
student_2.rate_lecture(lector_1, 'Java', 4)
student_1.rate_lecture(lector_2, 'Python', 8)
student_2.rate_lecture(lector_2, 'Java', 2)

print(lector_1.grades_lesson)
print(lector_2.grades_lesson)

print(lector_1)
print(lector_2)
print(lector_1.__lt__(lector_2))
print()
print(student_1)
print(student_2)
print(student_1.__lt__(student_2))


