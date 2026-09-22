import pytest
from grading_system import Student, Lecturer, Reviewer


@pytest.fixture
def student():
    """Базовый студент с двумя курсами в процессе."""
    s = Student('Ольга', 'Алёхина', 'Ж')
    s.courses_in_progress += ['Python', 'Java']
    return s


@pytest.fixture
def student_extra():
    """Второй студент для сравнений и агрегаций."""
    s = Student('Дмитрий', 'Сидоров', 'М')
    s.courses_in_progress += ['Python', 'C++']
    s.finished_courses += ['Введение в программирование']
    return s


@pytest.fixture
def lecturer():
    """Лектор, прикреплённый к Python и Java."""
    l = Lecturer('Иван', 'Иванов')
    l.courses_attached += ['Python', 'Java']
    return l


@pytest.fixture
def lecturer_extra():
    """Второй лектор для сравнений и агрегаций."""
    l = Lecturer('Николай', 'Титов')
    l.courses_attached += ['Python', 'C++']
    return l


@pytest.fixture
def reviewer():
    """Ревьюер, прикреплённый только к Python."""
    r = Reviewer('Пётр', 'Петров')
    r.courses_attached += ['Python']
    return r
