import unittest
from load_grade_book import load_gradebook_from_file
from load_grade_book import generate_gradebook_from_file_lines
from grade_book import GradeBook
from student import Student

class TestLoadGradeBook(unittest.TestCase):
  def test_load_gradebook_from_file_with_valid_file_returns_expected_grade_book(self):
    students = [
      Student([1,1,1], 1, 'Student 1'),
      Student([7,7,7], 7, 'Student 2'),
      Student([7,7,7], 7, 'Student 3'),
      Student([7,7,7], 7, 'Student 4'),
      Student([7,7,7], 7, 'Student 5'),
      Student([7,7,7], 7, 'Student 6'),
      Student([7,7,7], 7, 'Student 7'),
      Student([7,7,7], 7, 'Student 8'),
      Student([7,7,1], 5, 'Student 9'),
      Student([7,7,7], 7, 'Student 10'),
      Student([7,7,7], 7, 'Student 11'),
      Student([7,7,7], 7, 'Student 12'),
      Student([1,1,1], 1, 'Student 13'),
      Student([7,7,1], 5, 'Student 14'),
      Student([1,1,1], 1, 'Student 15'),
    ]
    grade_book = GradeBook(students)
    self.assertEqual(load_gradebook_from_file('grades.csv'), grade_book)

  def test_generate_gradebook_from_file_lines_when_no_lines_return_empty_array(self):
    self.assertEqual(generate_gradebook_from_file_lines([]), GradeBook([]))

  def test_generate_gradebook_from_file_lines_when_only_header_line_return_empty_array(self):
    self.assertEqual(generate_gradebook_from_file_lines([[",A1, A2, Avg"]]), GradeBook([]))

  def test_generate_gradebook_from_file_lines_when_one_grade_lines_return_one_student_array(self):
    lines = [[",", "A1", "A2", "A3", "Avg"], ["Student 1", "1", "2", "3", "2"]]
    students = [
      Student([1,2,3], 2, 'Student 1')
    ]
    self.assertEqual(generate_gradebook_from_file_lines(lines), GradeBook(students))

  def test_generate_gradebook_from_file_lines_when_two_grade_lines_return_two_student_array(self):
    lines = [["","A1", "A2", "A3", "Avg"], ["Student 1", "1", "2", "3", "2"], ["Student 2", "4", "4", "4", "4"]]
    students = [
      Student([1,2,3], 2, 'Student 1'),
      Student([4,4,4], 4, 'Student 2'),
    ]
    self.assertEqual(generate_gradebook_from_file_lines(lines), GradeBook(students))