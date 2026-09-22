"""Модуль grading_system: система оценок студентов и лекторов."""

from typing import Dict, List, Optional


def calculate_average(grades: Dict[str, List[int]]) -> float:
    """Считает средний балл по словарю оценок: {course: [grades]}."""
    all_grades = [
        grade
        for grades_list in grades.values()
        for grade in grades_list
    ]
    return sum(all_grades) / len(all_grades) if all_grades else 0.0


class Mentor:
    """Базовый класс для менторов (лекторы и ревьюеры)."""

    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.courses_attached: List[str] = []

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    """Класс лектора, который получает оценки от студентов."""

    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        self.grades: Dict[str, List[int]] = {}

    @property
    def average_grade(self) -> float:
        """Возвращает среднюю оценку за лекции."""
        return calculate_average(self.grades)

    def __str__(self) -> str:
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.average_grade:.2f}'
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade == other.average_grade

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade < other.average_grade

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade > other.average_grade


class Reviewer(Mentor):
    """Ревьюер, который ставит оценки за домашние задания."""

    def rate_hw(self, student: 'Student', course: str, grade: int) -> Optional[str]:
        if (
                isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress
                and 1 <= grade <= 10
        ):
            student.grades.setdefault(course, []).append(grade)
            return None
        return 'Ошибка'

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Student:
    """Студент, который учится и оценивает лекции."""

    def __init__(self, name: str, surname: str, gender: str) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses: List[str] = []
        self.courses_in_progress: List[str] = []
        self.grades: Dict[str, List[int]] = {}

    def add_finished_course(self, course_name: str) -> None:
        """Добавляет курс в завершённые."""
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer: Lecturer, course: str, grade: int) -> Optional[str]:
        if (
                isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached
                and 1 <= grade <= 10
        ):
            lecturer.grades.setdefault(course, []).append(grade)
            return None
        return 'Ошибка'

    @property
    def average_grade(self) -> float:
        """Возвращает среднюю оценку за домашние задания."""
        return calculate_average(self.grades)

    def __str__(self) -> str:
        courses_progress = ', '.join(self.courses_in_progress)
        courses_finished = ', '.join(self.finished_courses)
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade:.2f}\n'
            f'Курсы в процессе изучения: {courses_progress}\n'
            f'Завершенные курсы: {courses_finished}'
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return self.average_grade == other.average_grade

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return self.average_grade < other.average_grade

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return self.average_grade > other.average_grade


def average_grade_all_students(students: List[Student], course: str) -> float:
    """Возвращает среднюю оценку студентов по курсу."""
    all_grades: List[int] = []
    for student in students:
        if isinstance(student, Student):
            all_grades.extend(student.grades.get(course, []))
    return sum(all_grades) / len(all_grades) if all_grades else 0.0


def average_grade_all_lecturers(lecturers: List[Lecturer], course: str) -> float:
    """Возвращает среднюю оценку лекторов по курсу."""
    all_grades: List[int] = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            all_grades.extend(lecturer.grades.get(course, []))
    return sum(all_grades) / len(all_grades) if all_grades else 0.0