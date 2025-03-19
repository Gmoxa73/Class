from functools import total_ordering

def all_mid_bal_stud(list_stud, course):
    all_bal_stud = 0
    all_bal = 0
    for num, stud in enumerate(list_stud):
        if isinstance(stud, Student) and course in stud.courses_in_progress or stud.finished_courses:
            all_bal += stud.mid_bal()
            all_bal_stud = all_bal/(num + 1)
    return f'Средняя оценка студентов на курсе {course}: {all_bal_stud}\n'

def all_mid_bal_lec(list_lec, course):
    all_bal_lec = 0
    all_bal = 0
    for num, lec in enumerate(list_lec):
        if isinstance(lec, Lecturer) and course in lec.courses_attached:
            all_bal += lec.mid_bal()
            all_bal_lec = all_bal/(num + 1)
    return f'Средняя оценка лекторов на курсе {course}: {all_bal_lec}\n'


@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hwl(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __eq__(self, other):
        return f'Результат сравнения студентов: {self.mid_bal() == other.mid_bal()}\n'

    def __lt__(self, other):
        return f'Результат сравнения студентов: {self.mid_bal() < other.mid_bal()}\n'

    def mid_bal(self):
        a = 0
        val1 = 0
        for val in self.grades.values():
            for num, v in enumerate(val):
                val1 += v
                a = num + 1
        val = val1/a
        return val

    def __str__(self):
        return f'Студент:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.mid_bal()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __eq__(self, other):
        return f'Результат сравнения лекторов: {self.mid_bal() == other.mid_bal()}\n'

    def __lt__(self, other):
        return f'Результат сравнения лекторов: {self.mid_bal() < other.mid_bal()}\n'

    def mid_bal(self):
        a = 0
        val1 = 0
        for val in self.grades.values():
            for num, v in enumerate(val):
                val1 += v
                a = num + 1
        val = val1/a
        return val

    def __str__(self):
        return f'Лектор:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_bal()}\n'

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
        return f'Проверяющий:\nИмя: {self.name}\nФамилия: {self.surname}\n'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Java']

bad_student = Student('Bill', 'Sak', 'male')
bad_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lector = Lecturer('Bill', 'Weeks')
cool_lector.courses_attached += ['Python']

cl_lector = Lecturer('Mik', 'Will')
cl_lector.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 3)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(bad_student, 'Python', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 9)
cool_reviewer.rate_hw(bad_student, 'Python', 9)

best_student.rate_hwl(cool_lector,'Python',8)
best_student.rate_hwl(cool_lector,'Python',10)
best_student.rate_hwl(cool_lector,'Python',10)

bad_student.rate_hwl(cl_lector,'Python',5)
bad_student.rate_hwl(cl_lector,'Python',10)
bad_student.rate_hwl(cl_lector,'Python',4)

stud_list = [best_student, bad_student]
lec_list = [cool_lector, cl_lector]

print(best_student)
print(cool_reviewer)
print(cool_lector)
print(best_student == bad_student)
print(cool_lector == cl_lector)
print(all_mid_bal_stud(stud_list, 'Python'))
print(all_mid_bal_lec(lec_list, 'Python'))