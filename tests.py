import unittest
import check_grades

class TestCheckGrades(unittest.TestCase):
  def test_check_grades(self):
    self.assertEqual(check_grades.check_grades(), True)
