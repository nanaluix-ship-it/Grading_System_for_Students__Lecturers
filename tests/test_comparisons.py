import pytest

from grading_system import Student, Lecturer


class TestComparisons:
    def test_students_equal(self):
        s1 = Student('А', 'Б', 'Ж')
        s2 = Student('В', 'Г', 'М')
        assert s1 == s2

    def test_students_not_equal(self, student, student_extra, reviewer):
        reviewer.rate_hw(student, 'Python', 10)
        reviewer.rate_hw(student_extra, 'Python', 5)
        assert student != student_extra
        assert student > student_extra
        assert student_extra < student

    def test_lecturers_equal(self):
        l1 = Lecturer('А', 'Б')
        l2 = Lecturer('В', 'Г')
        assert l1 == l2

    def test_lecturers_not_equal(self, student, lecturer, lecturer_extra):
        student.rate_lecture(lecturer, 'Python', 9)
        student.rate_lecture(lecturer_extra, 'Python', 4)
        assert lecturer != lecturer_extra
        assert lecturer > lecturer_extra
        assert lecturer_extra < lecturer

    def test_student_vs_lecturer_no_crash(self):
        s = Student('А', 'Б', 'Ж')
        l = Lecturer('В', 'Г')
        # сравнение разных типов не должно падать
        assert (s == l) is False
        assert (s < l) is False
        assert (s > l) is False

    def test_student_vs_non_object(self):
        s = Student('А', 'Б', 'Ж')
        assert (s == 42) is False
        assert (s == 'string') is False
