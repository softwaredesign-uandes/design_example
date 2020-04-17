import unittest
import check_grades

class TestCheckGrades(unittest.TestCase):
  def test_check_grades_from_file_with_valid_file_returns_true(self):
    self.assertEqual(check_grades.check_grades_from_file('grades.csv'), True)

  def test_generate_students_from_file_lines_when_no_lines_return_empty_array(self):
    self.assertEqual(check_grades.generate_students_from_file_lines([]), [])

  def test_generate_students_from_file_lines_when_only_header_line_return_empty_array(self):
    self.assertEqual(check_grades.generate_students_from_file_lines([[",A1, A2, Avg"]]), [])

  def test_generate_students_from_file_lines_when_one_grade_lines_return_one_student_array(self):
    lines = [[",", "A1", "A2", "A3", "Avg"], ["Student 1", "1", "2", "3", "2"]]
    students = [{ "grades": [1,2,3], "file_average": 2}]
    self.assertEqual(check_grades.generate_students_from_file_lines(lines), students)

  def test_generate_students_from_file_lines_when_two_grade_lines_return_two_student_array(self):
    lines = [["","A1", "A2", "A3", "Avg"], ["Student 1", "1", "2", "3", "2"], ["Student 2", "4", "4", "4", "4"]]
    students = [{ "grades": [1,2,3], "file_average": 2 } , { "grades": [4,4,4], "file_average": 4 }]
    self.assertEqual(check_grades.generate_students_from_file_lines(lines), students)

  def test_check_student_grades_when_no_grades_and_zero_average_raises_exception(self):
    with self.assertRaises(ZeroDivisionError):
      check_grades.check_student_grades([], 0)

  def test_check_student_grades_when_one_grade_and_correct_average_returns_true(self):
    self.assertEqual(check_grades.check_student_grades([1], 1), True)

  def test_check_student_grades_when_one_grade_and_incorrect_average_returns_false(self):
    self.assertEqual(check_grades.check_student_grades([1], 10), False)

  def test_check_student_grades_when_thre_grades_and_correct_average_returns_true(self):
    self.assertEqual(check_grades.check_student_grades([1,1,4], 2), True)

  def test_check_all_grades_when_no_students_return_true(self):
    self.assertEqual(check_grades.check_all_grades([]), True)

  def test_check_all_grades_when_one_student_and_correct_average_return_true(self):
    students = [{ 'grades': [1,2,3], 'file_average': 2 }]
    self.assertEqual(check_grades.check_all_grades(students), True)

  def test_check_all_grades_when_one_student_and_incorrect_average_return_false(self):
    students = [{ 'grades': [1,2,3], 'file_average': 4 }]
    self.assertEqual(check_grades.check_all_grades(students), False)

  def test_check_all_grades_when_three_students_and_all_correct_average_return_true(self):
    students = [
      { 'grades': [1,2,3], 'file_average': 2 },
      { 'grades': [4,4,4], 'file_average': 4 },
      { 'grades': [5,3,1], 'file_average': 3 }
    ]
    self.assertEqual(check_grades.check_all_grades(students), True)

  def test_check_all_grades_when_three_students_and_one_incorrect_average_return_false(self):
    students = [
      { 'grades': [1,2,3], 'file_average': 2 },
      { 'grades': [4,4,4], 'file_average': 4 },
      { 'grades': [5,3,1], 'file_average': 7 }
    ]
    self.assertEqual(check_grades.check_all_grades(students), False)