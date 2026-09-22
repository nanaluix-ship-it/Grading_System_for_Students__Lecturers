def calculate_average(grades):
    """Считает средний балл по словарю оценок: {course: [grades]}"""
    all_grades = [
        grade
        for grades_list in grades.values()
        for grade in grades_list
    ]
    return sum(all_grades) / len(all_grades) if all_grades else 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    @property
    def average_grade(self):
        return calculate_average(self.grades)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade:.2f}')

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade == other.average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade > other.average_grade


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
                isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress
                and 1 <= grade <= 10
        ):
            student.grades.setdefault(course, []).append(grade)
            return
        return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_course(self, course_name):
        """Добавляет курс в завершённые."""
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if (
                isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached
                and 1 <= grade <= 10
        ):
            lecturer.grades.setdefault(course, []).append(grade)
            return
        return 'Ошибка'

    @property
    def average_grade(self):
        return calculate_average(self.grades)

    def __str__(self):
        courses_progress = ', '.join(self.courses_in_progress)
        courses_finished = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade:.2f}\n'
                f'Курсы в процессе изучения: {courses_progress}\n'
                f'Завершенные курсы: {courses_finished}')

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.average_grade == other.average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            return False
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            return False
        return self.average_grade > other.average_grade


def average_grade_all_students(students, course):
    """Возвращает среднюю оценку студентов по курсу (число)."""
    all_grades = []
    for student in students:
        if isinstance(student, Student):
            all_grades.extend(student.grades.get(course, []))
    return sum(all_grades) / len(all_grades) if all_grades else 0


def average_grade_all_lecturers(lecturers, course):
    """Возвращает среднюю оценку лекторов по курсу (число)."""
    all_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            all_grades.extend(lecturer.grades.get(course, []))
    return sum(all_grades) / len(all_grades) if all_grades else 0


if __name__ == '__main__':
    # Лекторы
    lecturer = Lecturer('Иван', 'Иванов')
    lecturer.courses_attached += ['Python', 'C++', 'Java']

    lecturer_1 = Lecturer('Николай', 'Титов')
    lecturer_1.courses_attached += ['C++', 'Java', 'Введение в программирование']

    lecturer_2 = Lecturer('Федор', 'Жигульский')
    lecturer_2.courses_attached += ['Python', 'Java']

    # Студенты
    student = Student('Алёхина', 'Ольга', 'Ж')
    student.courses_in_progress += ['Python', 'Java']
    student.add_finished_course('Введение в программирование')

    student_1 = Student('Дмитрий', 'Сидоров', 'М')
    student_1.courses_in_progress += ['Python', 'C++']
    student_1.add_finished_course('Введение в программирование')

    student_2 = Student('Степан', 'Мазута', 'М')
    student_2.courses_in_progress += ['Java', 'C++', 'Python']
    student_2.add_finished_course('Python')

    # Выставление оценок лекторам
    student.rate_lecture(lecturer, 'Python', 7)
    student.rate_lecture(lecturer_1, 'Java', 8)
    student.rate_lecture(lecturer_2, 'Java', 7)

    student_1.rate_lecture(lecturer, 'C++', 9)
    student_1.rate_lecture(lecturer_1, 'C++', 6)
    student_1.rate_lecture(lecturer_2, 'Python', 6)

    student_2.rate_lecture(lecturer, 'Java', 4)
    student_2.rate_lecture(lecturer_1, 'C++', 10)
    student_2.rate_lecture(lecturer_2, 'Java', 8)

    # Ревьюеры и оценки за ДЗ
    reviewer = Reviewer('Пётр', 'Петров')
    reviewer.courses_attached += ['Python', 'C++']

    reviewer_1 = Reviewer('Владимир', 'Кузнецов')
    reviewer_1.courses_attached += ['Java', 'C++']

    reviewer_2 = Reviewer('Илья', 'Самойлов')
    reviewer_2.courses_attached += ['Python', 'Введение в программирование']

    reviewer.rate_hw(student, 'Python', 5)
    reviewer.rate_hw(student_1, 'Python', 7)
    reviewer.rate_hw(student_2, 'C++', 7)

    reviewer_1.rate_hw(student, 'Java', 10)
    reviewer_1.rate_hw(student_1, 'C++', 4)
    reviewer_1.rate_hw(student_2, 'Java', 6)

    reviewer_2.rate_hw(student, 'Python', 6)
    reviewer_2.rate_hw(student_1, 'Python', 8)
    reviewer_2.rate_hw(student_2, 'Python', 7)

    # Списки для расчётов
    students = [student, student_1, student_2]
    lecturers = [lecturer, lecturer_1, lecturer_2]

    # Вывод объектов
    print(student)
    print(lecturer)
    print(reviewer)

    # Сравнение лекторов
    print(f'lecturer == lecturer_1: {lecturer == lecturer_1}')
    print(f'lecturer > lecturer_1: {lecturer > lecturer_1}')
    print(f'lecturer < lecturer_1: {lecturer < lecturer_1}')

    # Сравнение студентов
    print(f'student == student_1: {student == student_1}')
    print(f'student > student_1: {student > student_1}')
    print(f'student < student_1: {student < student_1}')

    # Средние по курсам
    avg_lect_java = average_grade_all_lecturers(lecturers, 'Java')
    avg_stud_python = average_grade_all_students(students, 'Python')

    print(f'Средняя оценка за лекции по курсу Java: {avg_lect_java:.2f}')
    print(f'Средняя оценка за домашние задания по курсу Python: {avg_stud_python:.2f}')
