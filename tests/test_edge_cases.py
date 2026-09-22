import pytest
from grading_system import (
    Student,
    Lecturer,
    Reviewer,
    Mentor,
    average_grade_all_students,
    average_grade_all_lecturers,
)


class TestAverageGradeAll:
    def test_students_by_course(self, student, student_extra, reviewer):
        reviewer.rate_hw(student, 'Python', 8)
        reviewer.rate_hw(student, 'Python', 10)
        reviewer.rate_hw(student_extra, 'Python', 6)
        reviewer.rate_hw(student_extra, 'Python', 4)

        result = average_grade_all_students([student, student_extra], 'Python')
        assert result == 7.0

    def test_students_no_grades_for_course(self, student, student_extra):
        result = average_grade_all_students([student, student_extra], 'Python')
        assert result == 0

    def test_students_partial_grades(self, student, student_extra, reviewer):
        """У одного студента есть оценки по курсу, у другого — нет."""
        reviewer.rate_hw(student, 'Python', 8)
        reviewer.rate_hw(student, 'Python', 6)

        result = average_grade_all_students([student, student_extra], 'Python')
        assert result == 7.0

    def test_students_empty_list(self):
        assert average_grade_all_students([], 'Python') == 0

    def test_lecturers_by_course(self, student, lecturer, lecturer_extra):
        student.rate_lecture(lecturer, 'Python', 7)
        student.rate_lecture(lecturer, 'Python', 9)
        student.rate_lecture(lecturer_extra, 'Python', 6)
        student.rate_lecture(lecturer_extra, 'Python', 10)

        result = average_grade_all_lecturers([lecturer, lecturer_extra], 'Python')
        assert result == 8.0

    def test_lecturers_no_grades_for_course(self, lecturer, lecturer_extra):
        result = average_grade_all_lecturers([lecturer, lecturer_extra], 'Python')
        assert result == 0

    def test_lecturers_empty_list(self):
        assert average_grade_all_lecturers([], 'Python') == 0


class TestStr:
    def test_student_str_contains_fields(self, student):
        text = str(student)
        assert 'Имя: Ольга' in text
        assert 'Фамилия: Алёхина' in text
        assert 'Средняя оценка за домашние задания' in text

    def test_lecturer_str_contains_fields(self, lecturer):
        text = str(lecturer)
        assert 'Имя: Иван' in text
        assert 'Фамилия: Иванов' in text
        assert 'Средняя оценка за лекции' in text

    def test_reviewer_str_no_average(self, reviewer):
        text = str(reviewer)
        assert 'Имя: Пётр' in text
        assert 'Фамилия: Петров' in text
        assert 'Средняя' not in text


class TestInheritance:
    def test_lecturer_is_mentor(self):
        l = Lecturer('Иван', 'Иванов')
        assert isinstance(l, Mentor)

    def test_reviewer_is_mentor(self):
        r = Reviewer('Пётр', 'Петров')
        assert isinstance(r, Mentor)

    def test_mentor_has_no_rate_hw(self):
        from grading_system import Mentor
        m = Mentor('Сергей', 'Сергеев')
        assert not hasattr(m, 'rate_hw')

    def test_lecturer_has_no_rate_hw(self):
        l = Lecturer('Иван', 'Иванов')
        assert not hasattr(l, 'rate_hw')
