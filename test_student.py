import unittest
from student import Student

class TestStudent(unittest.TestCase):
  def test_check_assignment_grades_when_no_grades_and_zero_average_raises_exception(self):
    with self.assertRaises(ZeroDivisionError):
      Student([], 0, 'a').check_assignment_grades()

  def test_check_assignment_grades_when_one_grade_and_correct_average_returns_true(self):
    self.assertEqual(Student([1], 1, 'a').check_assignment_grades(), True)

  def test_check_assignment_grades_when_one_grade_and_incorrect_average_returns_false(self):
    self.assertEqual(Student([1], 10, 'a').check_assignment_grades(), False)

  def test_check_assignment_grades_when_three_grades_and_correct_average_returns_true(self):
    self.assertEqual(Student([1,1,4], 2, 'a').check_assignment_grades(), True)

  def test_check_assignment_grades_when_three_float_grades_and_correct_average_returns_true(self):
    self.assertEqual(Student([4.0,4.1,4.2], 4.1, 'a').check_assignment_grades(), True)
  
  def test_calculate_final_grade_when_three_float_grades_returns_average(self):
    self.assertAlmostEqual(Student([4.0,4.1,4.2], 4.1, 'a').calculate_final_grade(), 4.1)

  def test_calculate_final_grade_when_all_grades_over_six_returns_seven(self):
    self.assertAlmostEqual(Student([6.0,6.1,6.2], 6.5, 'a').calculate_final_grade(), 6.5)

  def test_calculate_final_grade_when_one_grade_is_less_than_two_returns_three_point_nine(self):
    self.assertAlmostEqual(Student([7.0,7.0,1.2], 3.9, 'a').calculate_final_grade(), 3.9)