import csv
from student import Student
from grade_book import GradeBook

def load_gradebook_from_file(file_path):
  with open(file_path, 'r') as grades_file:
    reader = csv.reader(grades_file, delimiter=',')
    file_lines = list(reader)
    return generate_gradebook_from_file_lines(file_lines)
    
def generate_gradebook_from_file_lines(file_lines):
  students = []
  for line in file_lines[1:]:
    name = line[0]
    file_average = float(line[-1])
    grades = map(float, line[1:-1])

    student = Student(grades, file_average, name)
    students.append(student)
  return GradeBook(students)