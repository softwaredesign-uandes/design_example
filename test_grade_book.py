import unittest
from grade_book import GradeBook
from student import Student

class TestGradeBook(unittest.TestCase):
  def test_check_assignment_grades_when_no_students_return_true(self):
    self.assertEqual(GradeBook([]).check_assignment_grades(), True)

  def test_check_assignment_grades_when_one_student_and_correct_average_return_true(self):
    students = [Student([1,2,3], 2, 'a')]
    self.assertEqual(GradeBook(students).check_assignment_grades(), True)

  def test_check_assignment_grades_when_one_student_and_incorrect_average_return_false(self):
    students = [Student([1,2,3], 4, 'a')]
    self.assertEqual(GradeBook(students).check_assignment_grades(), False)

  def test_check_assignment_grades_when_three_students_and_all_correct_average_return_true(self):
    students = [
      Student([1,2,3], 2, 'a'),
      Student([4,4,4], 4, 'b'),
      Student([5,3,1], 3, 'c')
    ]
    self.assertEqual(GradeBook(students).check_assignment_grades(), True)

  def test_check_assignment_grades_when_three_students_and_one_incorrect_average_return_false(self):
    students = [
      Student([1,2,3], 2, 'a'),
      Student([4,4,4], 4, 'b'),
      Student([5,3,1], 7, 'c')
    ]
    self.assertEqual(GradeBook(students).check_assignment_grades(), False)