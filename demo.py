from grading_system import (
    Lecturer,
    Student,
    Reviewer,
    average_grade_all_students,
    average_grade_all_lecturers,
)

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

# Ревьюеры и оценки за ДЗ
reviewer = Reviewer('Пётр', 'Петров')
reviewer.courses_attached += ['Python', 'C++']

reviewer_1 = Reviewer('Владимир', 'Кузнецов')
reviewer_1.courses_attached += ['Java', 'C++']

reviewer_2 = Reviewer('Илья', 'Самойлов')
reviewer_2.courses_attached += ['Python', 'Введение в программирование']

# Выставление оценок
reviewer.rate_hw(student, 'Python', 5)
reviewer.rate_hw(student_1, 'Python', 7)
reviewer.rate_hw(student_2, 'C++', 7)

reviewer_1.rate_hw(student, 'Java', 10)
reviewer_1.rate_hw(student_1, 'C++', 4)
reviewer_1.rate_hw(student_2, 'Java', 6)

reviewer_2.rate_hw(student, 'Python', 6)
reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 7)

student.rate_lecture(lecturer, 'Python', 7)
student.rate_lecture(lecturer_1, 'Java', 8)
student.rate_lecture(lecturer_2, 'Java', 7)

student_1.rate_lecture(lecturer, 'C++', 9)
student_1.rate_lecture(lecturer_1, 'C++', 6)
student_1.rate_lecture(lecturer_2, 'Python', 6)

student_2.rate_lecture(lecturer, 'Java', 4)
student_2.rate_lecture(lecturer_1, 'C++', 10)
student_2.rate_lecture(lecturer_2, 'Java', 8)

# Вывод
print(student)
print(lecturer)
print(reviewer)

print(f'lecturer == lecturer_1: {lecturer == lecturer_1}')
print(f'lecturer > lecturer_1: {lecturer > lecturer_1}')
print(f'lecturer < lecturer_1: {lecturer < lecturer_1}')

print(f'student == student_1: {student == student_1}')
print(f'student > student_1: {student > student_1}')
print(f'student < student_1: {student < student_1}')

avg_lect_java = average_grade_all_lecturers([lecturer, lecturer_1, lecturer_2], 'Java')
avg_stud_python = average_grade_all_students([student, student_1, student_2], 'Python')

print(f'Средняя оценка за лекции по курсу Java: {avg_lect_java:.2f}')
print(f'Средняя оценка за домашние задания по курсу Python: {avg_stud_python:.2f}')