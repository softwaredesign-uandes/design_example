import csv

def check_grades_from_file(file_path):
  with open(file_path, 'r') as grades_file:
    reader = csv.reader(grades_file, delimiter=',')
    file_lines = list(reader)
    students = generate_students_from_file_lines(file_lines)
    return check_all_grades(students)
    
def generate_students_from_file_lines(file_lines):
  students = []
  for line in file_lines[1:]:
    file_average = int(line[-1])
    grades = map(int, line[1:-1])

    student = {}
    student['grades'] = grades
    student['file_average'] = file_average
    students.append(student)
  return students

def check_student_grades(grades, file_average):
  calculated_average = sum(grades) / len(grades) 

  return file_average == calculated_average

def check_all_grades(students):
  for student in students:
    if not check_student_grades(student['grades'], student['file_average']):
      return False
  return True



print check_grades_from_file("grades.csv")
