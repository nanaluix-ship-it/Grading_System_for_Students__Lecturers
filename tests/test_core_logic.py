import pytest
from grading_system import calculate_average


class TestCalculateAverage:
    def test_empty_dict(self):
        assert calculate_average({}) == 0

    def test_single_course_single_grade(self):
        assert calculate_average({'Python': [8]}) == 8.0

    def test_single_course_multiple_grades(self):
        assert calculate_average({'Python': [6, 8, 10]}) == 8.0

    def test_multiple_courses(self):
        grades = {'Python': [7, 9], 'Java': [6, 10]}
        assert calculate_average(grades) == 8.0

    def test_all_zeros(self):
        assert calculate_average({'Python': [0, 0, 0]}) == 0.0


class TestRateLecture:
    def test_valid_grade(self, student, lecturer):
        result = student.rate_lecture(lecturer, 'Python', 8)
        assert result is None
        assert lecturer.grades['Python'] == [8]

    def test_grade_below_one(self, student, lecturer):
        result = student.rate_lecture(lecturer, 'Python', 0)
        assert result == 'Ошибка'
        assert 'Python' not in lecturer.grades

    def test_grade_above_ten(self, student, lecturer):
        result = student.rate_lecture(lecturer, 'Python', 11)
        assert result == 'Ошибка'
        assert 'Python' not in lecturer.grades

    def test_course_not_in_progress(self, student, lecturer):
        student.courses_in_progress = []
        result = student.rate_lecture(lecturer, 'Python', 8)
        assert result == 'Ошибка'

    def test_boundary_grade_one(self, student, lecturer):
        result = student.rate_lecture(lecturer, 'Python', 1)
        assert result is None
        assert lecturer.grades['Python'] == [1]

    def test_boundary_grade_ten(self, student, lecturer):
        result = student.rate_lecture(lecturer, 'Python', 10)
        assert result is None
        assert lecturer.grades['Python'] == [10]


class TestRateHw:
    def test_valid_grade(self, reviewer, student):
        result = reviewer.rate_hw(student, 'Python', 7)
        assert result is None
        assert student.grades['Python'] == [7]

    def test_grade_below_one(self, reviewer, student):
        result = reviewer.rate_hw(student, 'Python', 0)
        assert result == 'Ошибка'
        assert 'Python' not in student.grades

    def test_grade_above_ten(self, reviewer, student):
        result = reviewer.rate_hw(student, 'Python', 11)
        assert result == 'Ошибка'
        assert 'Python' not in student.grades

    def test_course_not_attached(self, reviewer, student):
        result = reviewer.rate_hw(student, 'Java', 8)
        assert result == 'Ошибка'
        assert 'Java' not in student.grades
