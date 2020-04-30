class Student:
  def __init__(self, assignment_grades, assignment_final_grade, name):
    self.assignment_grades = assignment_grades
    self.assignment_final_grade = assignment_final_grade
    self.name = name
  
  def __eq__(self, other):
    if self.name != other.name:
      return False 
    if self.assignment_final_grade != other.assignment_final_grade:
      return False
    if len(self.assignment_grades) != len(other.assignment_grades):
      return False
    for i in range(len(self.assignment_grades)):
      if self.assignment_grades[i] != other.assignment_grades[i]:
        return False
    return True
  
  def calculate_final_grade(self):
    average = sum(self.assignment_grades) / len(self.assignment_grades) 
    if len(filter(lambda g: g >= 6, self.assignment_grades)) == len(self.assignment_grades):
      return 7.0
    elif len(filter(lambda g: g <= 2, self.assignment_grades)) >= 1:
      return min([3.9, average])
    else:
      return average

  def check_assignment_grades(self):
    def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
      return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol) 

    return is_close(self.assignment_final_grade, self.calculate_final_grade()) 